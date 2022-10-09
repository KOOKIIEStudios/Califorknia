"""
    Tiles that trigger specific events
"""

import pygame

from califorknia.constants.constants import TILE_SIZE


class Tile:
    _id: int

    def __init__(
            self,
            tile_id: int = 0,
            traversable: bool = True,
    ):
        self._id = tile_id
        self._traversable = traversable

    @property
    def id(self):
        return self._id

    @property
    def traversable(self):
        return self._traversable

    def on_player_walk(self):
        pass

    def __repr__(self):
        return f"Tile([id: {self.id}])"
