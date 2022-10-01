from typing import List

import pygame

from califorknia.entities.direction import Direction
from califorknia.entities.dishes.dish import Dish
from califorknia.entities.entity import Entity
from califorknia.game.item import Item
from califorknia.map.map import Map


class Player(Entity):
    _inventory: List[Item] = []
    _dishes: List[Dish] = []
    _map: Map = None

    def __init__(self, name: str, sprite: str = None, map_: Map = None, pos: tuple[int, int] = (0, 0)):
        super().__init__(name, sprite, pos)
        self._map = map_

    def listen_input(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self._move(Direction.UP)
        if key_pressed[pygame.K_DOWN]:
            self._move(Direction.DOWN)
        if key_pressed[pygame.K_LEFT]:
            self._move(Direction.LEFT)
        if key_pressed[pygame.K_RIGHT]:
            self._move(Direction.RIGHT)

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
