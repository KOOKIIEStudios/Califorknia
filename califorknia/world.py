"""This module holds all objects currently active in the game world

The World object instantiates the other entities, which allows them to not
need to know about the implementation of each other (i.e. Player does not need
to know what else is in the map until we tell them).
"""
from typing import Union

from pygame import Surface

import logger
from califorknia.maps.special_tiles.grasstile import GrassTile
from califorknia.maps.special_tiles.watertile import WaterTile
from califorknia.maps.tile import Tile
from constants.constants import PLAYER_ID
from constants.direction import Direction
from entities.npc import Npc
from entities.player import Player
from maps.map import Map
from utils import render_world
from utils.yaml import load_npc_metadata

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
        self._active_map.parse_map("test_map")

        self._player = Player("Player", pos=(0, 0))

        self._special_tiles: dict[int, Tile] = {
            10: GrassTile(),
            11: WaterTile()
        }

    def init_active_entities(self, selected_map: str) -> None:
        active_entities_attributes = load_npc_metadata(selected_map)
        if not active_entities_attributes:
            log.debug(f"[{selected_map}] There are no NPCs to load.")
            return
        # At the moment these are all NPCs:
        for entity_id, attributes in active_entities_attributes.items():
            self._active_npcs[entity_id] = Npc(
                entity_id,
                attributes.get("name"),
                (attributes.get("x"), attributes.get("y")),
            )

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

    def _move_player(self, direction: Direction) -> None:
        """Update Player and Map objects"""
        player = self._get_player()
        new_x, new_y = player.get_new_coord(direction)
        # log.debug(player)
        if self.active_map.is_out_of_bounds(new_x, new_y):
            # log.debug(f"Out of bounds! Requested X: {new_x}, requested Y: {new_y}")
            return  # short-circuit if out of map boundaries
        next_tile_id = self.active_map.tiles[new_y][new_x]
        if next_tile_id in self._special_tiles:
            tile_object = self._special_tiles[next_tile_id]
            if tile_object.traversable:
                player.move(direction)  # update player x/y-coord attributes
                tile_object.on_player_walk()
        else:
            player.move(direction)  # update player x/y-coord attributes
        # log.debug(player)
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
        if entity_id == PLAYER_ID:
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
            self._active_map
        )
