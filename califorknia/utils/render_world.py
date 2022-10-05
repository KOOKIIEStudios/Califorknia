"""Render the world's entities with PyGame"""
from typing import Union

import pygame
from pygame import Surface
from pygame.surface import SurfaceType

import logger
from constants.constants import TILE_SIZE
from entities.npc import Npc
from entities.player import Player

from califorknia.maps.map import Map
from utils.yaml import load_tile_spites, TILES_FOLDER

log = logger.get_logger(__name__)


def _init_tile_dictionary() -> dict[int, Union[Surface, SurfaceType]]:
    buffer = {}
    tile_file_name_dictionary = load_tile_spites()
    for tile_id, file_name in tile_file_name_dictionary.items():
        buffer[tile_id] = pygame.image.load(TILES_FOLDER.joinpath(file_name))
    return buffer


TILE_MAP = _init_tile_dictionary()


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
    for row_number, row in enumerate(active_map.tiles):
        for column_number, column in enumerate(row):
            if column > 0:
                image = TILE_MAP.get(column)
                if image is None:
                    log.warning(f"TILE NOT FOUND! Row {row_number}, column {column_number}")
                    continue
                surface.blit(
                    image, (column_number * TILE_SIZE, row_number * TILE_SIZE)
                )
            # TODO: Action for tile id <= 0


def render_world(
        player: Player, npcs: dict[int, Npc], surface: Surface, active_map: Map
) -> None:
    _render_map(active_map, surface)
    _render_entities(player, npcs, surface)
