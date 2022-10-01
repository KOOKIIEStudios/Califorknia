"""This module holds the Player class.

The player object implements the various ways that the player of the game
can interact with the game, such as movement using the arrow keys.
"""
import pygame

from califorknia.entities.direction import Direction
from califorknia.entities.dishes.dish import Dish
from califorknia.entities.entity import Entity
from califorknia.game.item import Item
from califorknia.map.map import Map


class Player(Entity):
    """This class models the single player interacting with the game."""
    _inventory: list[Item] = []
    _dishes: list[Dish] = []
    _map: Map = None

    def __init__(
        self,
        name: str,
        sprite: str = None,
        pos: tuple[int, int] = (0, 0),
        map_: Map = None,
    ):
        super().__init__(name, sprite, pos)
        self._map = map_

    def listen_input(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
            self._move(Direction.UP)
        if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
            self._move(Direction.DOWN)
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
            self._move(Direction.LEFT)
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
            self._move(Direction.RIGHT)

        # TODO: Other keys like pause/menu/run

    def _move(self, direction: Direction):
        match direction:
            case Direction.UP:
                self.y -= 1
            case Direction.DOWN:
                self.y += 1
            case Direction.LEFT:
                self.x -= 1
            case Direction.RIGHT:
                self.x += 1
        # TODO: This should render the player move over to the new tile
        self._map.tiles[self.y][self.x] = self

    @property
    def x(self):
        return self._pos[0]

    @x.setter
    def x(self, new_x: int):
        self._set_pos(new_x, self.y)

    @property
    def y(self):
        return self._pos[1]

    @y.setter
    def y(self, new_y: int):
        self._set_pos(self.x, new_y)

    def _set_pos(self, x: int, y: int):
        self._pos = (x, y)
