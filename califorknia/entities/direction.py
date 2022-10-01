"""This module holds movement-related enums

When a key-down event or a keypress occurs, the input listener needs to
convey the direction associated with that key to the player's `_move` method.
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
