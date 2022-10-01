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
