"""Render the world's entities with PyGame"""
from typing import Union

from pygame import draw, Surface

import logger
from constants.constants import TILE_SIZE
from entities.npc import Npc
from entities.player import Player

log = logger.get_logger(__name__)


def _render_entity(entity: Union[Player, Npc], surface: Surface) -> None:
    color = (127, 0, 7)  # NPC color
    entity_size = 32
    if isinstance(entity, Player):
        color = (255, 255, 255)  # White for Player
    draw.rect(
        surface,
        color,
        (entity.x * TILE_SIZE, entity.y * TILE_SIZE, entity_size, entity_size),
    )


def _render_entities(
    player: Player, npcs: dict[int, Npc], surface: Surface
) -> None:
    _render_entity(player, surface)
    if not npcs.values():
        return  # no NPCs
    for npc in npcs.values():
        _render_entity(npc, surface)


def render_world(
    player: Player, npcs: dict[int, Npc], surface: Surface
) -> None:
    surface.fill((0, 0, 0))  # clear the screen before drawing entities
    _render_entities(player, npcs, surface)
