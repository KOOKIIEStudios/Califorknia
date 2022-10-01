"""This module holds movement-related enums

When a key-down event or a keypress occurs, the input listener needs to
convey the direction associated with that key to the various directional methods
in Player or World.
This module is used for conveying the direction in an immutable form that is
resistant to typos.
"""
from enum import Enum


class Direction(Enum):
    """This Enum models the direction of the player's movement"""
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
