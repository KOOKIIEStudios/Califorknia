"""
    Map will be grid-based and will be a 2D array of tiles.
    [ [] [] [] [] []
      [] [] [] [] []
      [] [] [] [] [] ]
"""
import logger

from califorknia.constants import TILE_SIZE, WIDTH, HEIGHT


log = logger.get_logger(__name__)


class Map:
    """This class models the in-game maps

    The player is only in one map at a time, and maps are located adjacent to
    one another. Each map is modeled using a 2D List, representing a series of
    tiles on a 2D plane; each cell in the list can hold an integer to represent
    what is on that tile.
    `0` represents an empty/traversable tile. All humanoid entities
    on the map will have an ID in the corresponding cell that they're located
    on. Special tiles with special properties will have their own IDs.
    """
    _tiles: list[list] = []
    _window = None

    def __init__(self, window):
        self._window = window
        self.init_tiles()

    def init_tiles(self):
        row = [0 for _ in range(WIDTH // TILE_SIZE)]
        self._tiles = [row for _ in range(HEIGHT // TILE_SIZE)]
        # log.debug(self._tiles)

    @property
    def tiles(self):
        return self._tiles

    def render_map(self):
        for row in self._tiles:
            for entity in row:
                if entity != 0:
                    entity.render(self._window)

    def place_entity(self, entity, x, y):
        self._tiles[y][x] = entity

    # TODO: __str__
