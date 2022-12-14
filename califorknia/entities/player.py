"""This module holds the Player class.

The player object implements the various attributes that a player's in-game
character should have.
"""
import logger

from constants.constants import PLAYER_ID, PLAYER_BASE_VELOCITY, PLAYER_SPEED_MODIFIER
from constants.direction import Direction
from califorknia.entities.dishes.dish import Dish
from califorknia.entities.entity import Entity
from califorknia.game.item import Item


log = logger.get_logger(__name__)


class Player(Entity):
    """This class models the single player interacting with the game."""
    _inventory: list[Item] = []
    _dishes: list[Dish] = []
    _base_velocity: int = PLAYER_BASE_VELOCITY
    _run_modifier: int = PLAYER_SPEED_MODIFIER
    _run_flag: bool = False  # is currently running

    def __init__(
        self,
        name: str,
        pos: tuple[int, int] = (0, 0),
    ):
        super().__init__(PLAYER_ID, name, pos)

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

    def _get_velocity(self):
        velocity = self.base_velocity
        if self.run_flag:
            velocity = self.base_velocity * self.run_modifier
        # log.debug(f"Current player velocity: {velocity}")
        return velocity

    def get_new_coord(self, direction: Direction) -> tuple[int, int]:
        velocity = self._get_velocity()
        match direction:
            case Direction.UP:
                return self.x, self.y - velocity
            case Direction.DOWN:
                return self.x, self.y + velocity
            case Direction.LEFT:
                return self.x - velocity, self.y
            case Direction.RIGHT:
                return self.x + velocity, self.y

    def move(self, direction: Direction):
        new_x, new_y = self.get_new_coord(direction)
        self.x = new_x
        self.y = new_y
        # TODO: This should render the player move over to the new tile

    def __repr__(self):
        text = f"Player([id: {self.id}, name: {self.name}, " \
               f"pos: {self._pos}, velocity: {self._get_velocity()}, " \
               f"dishes: TODO, items: TODO])"
        return text
