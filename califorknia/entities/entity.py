"""This module holds the Entity abstract class, and relevant utility functions

Entities are humanoid creatures in the game. This module also houses other
utility/static functions like accessors.
"""


class Entity:
    """This is an abstract class that models any humanoid entities in-game.

    This includes Aliens, Players, and NPCs.
    Player and NPCs will inherit from this class.
    """
    _id: int
    _sprite: str  # Consider using Path object
    _name: str
    _pos: tuple[int, int]  # x, y

    def __init__(
        self,
        entity_id: int = 0,
        name: str = "",
        sprite: str = "",
        pos: tuple[int, int] = (0, 0),
    ):
        # Suggest init with automatically generated unique name/sprite
        #   instead of empty string
        self._id = entity_id
        self._name = name
        self._sprite = sprite
        self._pos = pos

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def x(self):
        """This refers to the column number.

         The tiles on the maps are a 2D grid, and this refers to the column
         number of the tile that the player is currently on.
         """
        return self._pos[0]

    @x.setter
    def x(self, new_x: int):
        self._set_pos(new_x, self.y)

    @property
    def y(self):
        """This refers to the row number.

        The tiles on the maps are a 2D grid, and this refers to the row
        number of the tile that the player is currently on.
        """
        return self._pos[1]

    @y.setter
    def y(self, new_y: int):
        self._set_pos(self.x, new_y)

    def _set_pos(self, x: int, y: int):
        self._pos = (x, y)

    # TODO: Sprite property that returns the currently active sprite

    def __repr__(self):
        return f"Entity([id: {self.id}, name: {self.name}, " \
               f"sprite: {self._sprite}, pos: {self._pos}])"
