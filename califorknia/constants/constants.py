"""This module holds various global constants"""
from typing import Any

from utils.yaml import load_constants, SOURCE_FOLDER

TILE_SIZE = 32  # every size of an entity or block in this game is 32x32
ENTITY_SIZE = 32
WINDOW_NAME = "Califorknia"
SETTINGS: dict[str, Any] = load_constants()

TILE_ASSETS_FOLDER = SOURCE_FOLDER.joinpath("assets").joinpath("tiles")
ENTITY_ASSETS_FOLDER = SOURCE_FOLDER.joinpath("assets").joinpath("entities")

# Player constants
PLAYER_ID: int = 1
PLAYER_BASE_VELOCITY: int = 1
PLAYER_SPEED_MODIFIER: int = 2
