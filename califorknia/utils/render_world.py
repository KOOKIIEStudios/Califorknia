"""Render the world's entities with PyGame"""
from typing import Union

import pygame
from pygame import draw, Surface

import logger
from constants.constants import TILE_SIZE
from entities.npc import Npc
from entities.player import Player

from califorknia.maps.map import Map

log = logger.get_logger(__name__)


def _render_entity(entity, surface: Surface) -> None:
    entity_size = 32
    surface.blit(entity.image, (entity.x * entity_size, entity.y * entity_size))


def _render_entities(
        player: Player, npcs: dict[int, Npc], surface: Surface
) -> None:
    _render_entity(player, surface)
    if not npcs.values():
        return  # no NPCs
    for npc in npcs.values():
        _render_entity(npc, surface)


def _render_map(active_map: Map, surface: Surface) -> None:
    for y in range(len(active_map.tiles)):
        row = active_map.tiles[y]
        for x in range(len(row)):
            tile = row[x]
            if tile > 0:
                image = tiles_to_render.get(tile)
                if image is None:
                    continue
                surface.blit(tiles_to_render.get(tile), (x * TILE_SIZE, y * TILE_SIZE))


def render_world(
        player: Player, npcs: dict[int, Npc], surface: Surface, active_map: Map
) -> None:
    # surface.fill((0, 0, 0))  # clear the screen before drawing entities
    _render_map(active_map, surface)
    _render_entities(player, npcs, surface)


# TODO: autogenerate this map for all tiles in assets folder
tiles_to_render = {
    49: pygame.transform.scale(pygame.image.load("assets/tile_0049.png"), (TILE_SIZE, TILE_SIZE)),
}
