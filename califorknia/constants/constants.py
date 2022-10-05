"""This module holds various global constants"""
from typing import Any

from utils.yaml import load_constants

TILE_SIZE = 32  # every size of an entity or block in this game is 32x32
WINDOW_NAME = "Califorknia"
SETTINGS: dict[str, Any] = load_constants()
