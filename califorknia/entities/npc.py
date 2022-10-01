"""This module contains the Npc class.

The Npc class models non-playing characters, like instructional characters
that give tutorials, shops, and Aliens that can be challenged to battle.
"""
import logger

from califorknia.entities.entity import Entity


log = logger.get_logger(__name__)


class Npc(Entity):
    """This class models NPC entities in-game

    Attributes:
    """

    def __init__(
        self,
        entity_id: int,
        name: str,
        sprite: str = None,
        pos: tuple[int, int] = (0, 0),
    ):
        super().__init__(entity_id, name, sprite, pos)
        # TODO: Consider making sprite the Path object for a directory
        #   Since there will probably be multiple sprites for one NPC

    def __repr__(self):
        return f"Npc([id: {self.id}, name: {self.name}, sprite: {self._sprite}, pos: {self._pos}])"

    pass
