"""
    This represents any humanoid in the game, Aliens, Players, and NPCs.
    Player and NPCs will inherit from this class.
"""
import pygame

from califorknia.constants import TILE_SIZE


class Entity:
    """This is an abstract class that models any humanoid entities in-game."""
    _id: int = 0
    _sprite: str = "URL/TO/SPRITE"  # Consider using Path object
    _name: str = ""
    _pos: tuple[int, int] = (0, 0)  # x, y

    def __init__(
        self, name: str = "", sprite: str = "",  pos: tuple[int, int] = (0, 0)
    ):
        # Suggest init with automatically generated unique name/sprite
        #   instead of empty string
        self._sprite = sprite
        self._name = name
        self._pos = pos

    def render(self, window_):
        pygame.draw.rect(
            window_,
            (255, 255, 255),
            (self._pos[0] * TILE_SIZE, self._pos[1] * TILE_SIZE, 32, 32),
        )

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def x(self):
        """This refers to the column number.

         The tiles on the map are a 2D grid, and this refers to the column
         number of the tile that the player is currently on.
         """
        return self._pos[0]

    @x.setter
    def x(self, new_x: int):
        self._set_pos(new_x, self.y)

    @property
    def y(self):
        """This refers to the row number.

        The tiles on the map are a 2D grid, and this refers to the row
        number of the tile that the player is currently on.
        """
        return self._pos[1]

    @y.setter
    def y(self, new_y: int):
        self._set_pos(self.x, new_y)

    def _set_pos(self, x: int, y: int):
        self._pos = (x, y)

    # TODO: Sprite property that returns the currently active sprite
