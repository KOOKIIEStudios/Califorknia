"""This module holds the Player class.

The player object implements the various attributes that a player's in-game
character should have.
"""
import logger

from constants.direction import Direction
from califorknia.entities.dishes.dish import Dish
from califorknia.entities.entity import Entity
from califorknia.game.item import Item


log = logger.get_logger(__name__)


class Player(Entity):
    """This class models the single player interacting with the game."""
    _inventory: list[Item] = []
    _dishes: list[Dish] = []
    _base_velocity: int = 1
    _run_modifier: int = 2
    _run_flag: bool = False  # is currently running

    def __init__(
        self,
        name: str,
        sprite: str = None,
        pos: tuple[int, int] = (0, 0),
    ):
        super().__init__(1, name, sprite, pos)

    @property
    def base_velocity(self) -> int:
        return self._base_velocity

    @property
    def run_modifier(self) -> int:
        return self._run_modifier

    @property
    def run_flag(self) -> bool:
        return self._run_flag

    @run_flag.setter
    def run_flag(self, flag: bool):
        self._run_flag = flag

    def move(self, direction: Direction):
        velocity = self.base_velocity
        if self.run_flag:
            velocity = self.base_velocity * self.run_modifier
        match direction:
            case Direction.UP:
                self.y -= velocity
            case Direction.DOWN:
                self.y += velocity
            case Direction.LEFT:
                self.x -= velocity
            case Direction.RIGHT:
                self.x += velocity
        # TODO: This should render the player move over to the new tile
