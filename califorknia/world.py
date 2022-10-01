"""This module holds all objects currently active in the game world

The World object instantiates the other entities, which allows them to not
need to know about the implementation of each other (i.e. Player does not need
to know what else is in the map until we tell them).
"""
from typing import Any, Union

from pygame import Surface

import logger
from constants.direction import Direction
from entities.entity import Entity
from entities.npc import Npc
from entities.player import Player
from maps import metadata
from maps.map import Map
from utils import render_world

log = logger.get_logger(__name__)


class World:
    """This class holds and interacts with active entities

    The World object instantiates and holds active entities. It also takes in
    stimulus from external events, and passes them on to the entities it holds.
    """
    _window: Surface
    _active_map: Map
    _menu_flag: bool = False  # Whether the ESC or Player menu is open

    def __init__(self, screen: Surface, selected_map: str = None):
        self._window = screen
        self._active_map = Map(selected_map)

        self._active_npcs: dict[int, Npc] = {}
        self.init_active_entities(self._active_map.name)

        self._player = Player("Player", pos=(0, 0))
        self._place_entity_on_map(self._player)

    @staticmethod
    def get_active_entities_ids(selected_map: str) -> dict[int, dict[str, Any]]:
        """Get the list of NPCs in the current maps"""
        return metadata.ENTITIES.get(selected_map, {})

    def init_active_entities(self, selected_map: str) -> None:
        active_entities_attributes = self.get_active_entities_ids(selected_map)
        # At the moment these are all NPCs:
        for entity_id, attributes in active_entities_attributes.items():
            self._active_npcs[entity_id] = Npc(
                entity_id,
                attributes.get("name"),
                attributes.get("sprite"),
                (attributes.get("x"), attributes.get("y")),
            )
        # TODO: Place them on the map

    @property
    def active_map(self) -> Map:
        return self._active_map

    @active_map.setter
    def active_map(self, new_map: Map) -> None:
        self._active_map = new_map

    @property
    def menu_flag(self) -> bool:
        return self._menu_flag

    @menu_flag.setter
    def menu_flag(self, new_flag: bool) -> None:
        self._menu_flag = new_flag

    def toggle_menu_flag(self) -> None:
        self.menu_flag = not self.menu_flag

    def _get_player(self):
        return self._player

    def _place_entity_on_map(self, entity: Entity):
        # TODO: Centre the entity instead of aligning top left
        return self.active_map.place_entity(entity.id, entity.x, entity.y)

    def _move_player(self, direction: Direction) -> None:
        """Update Player and Map objects"""
        player = self._get_player()
        self.active_map.reset_tile(player.x, player.y)  # clear player from map
        # log.debug(player)
        player.move(direction)  # update player x/y-coord attributes
        self._place_entity_on_map(player)  # replace player
        # log.debug(self.active_map)

    def handle_direction(self, direction: Direction) -> None:
        if not self.menu_flag:
            return self._move_player(direction)
        # TODO: Change menu highlight based on direction

    def handle_selection(self):
        pass  # TODO: Handle menu item selection

    def start_player_run(self):
        player = self._get_player()
        player.run_flag = True

    def stop_player_run(self):
        player = self._get_player()
        player.run_flag = False

    def get_active_entity(self, entity_id: int) -> Union[Player, Npc, None]:
        if entity_id == 1:
            return self._get_player()

        entity = self._active_npcs.get(entity_id)
        if entity is None:
            log.warning(f"Invalid entity ID! ID: {entity_id}")
            return
        return entity

    def render_map(self) -> None:
        render_world.render_world(
            self._get_player(),
            self._active_npcs,
            self._window,
        )
