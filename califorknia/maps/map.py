"""
    Map will be grid-based and will be a 2D array of tiles.
    [ [] [] [] [] []
      [] [] [] [] []
      [] [] [] [] [] ]
"""
import logger

from califorknia.constants.constants import TILE_SIZE, WIDTH, HEIGHT

log = logger.get_logger(__name__)


class Map:
    """This class models the in-game maps

    The player is only in one maps at a time, and maps are located adjacent to
    one another. Each maps is modeled using a 2D List, representing a series of
    tiles on a 2D plane; each cell in the list can hold an integer to represent
    what is on that tile.
    `0` represents an empty/traversable tile. All humanoid entities
    on the maps will have an ID in the corresponding cell that they're located
    on. Special tiles with special properties will have their own IDs.
    """
    _tiles: list[list[int]] = []

    def __init__(self, map_name: str):
        if not map_name:
            self.name = "test_map"
        else:
            self.name = map_name
        self.init_tiles()

    def init_tiles(self):
        self._tiles = [[0 for _ in range(WIDTH // TILE_SIZE)] for _ in range(HEIGHT // TILE_SIZE)]
        # log.debug(self)

    def parse_map(self, map_name: str):
        self._tiles = []
        with open('maps/custommaps/' + map_name + ".txt") as map_file:
            for line in map_file:
                row = [int(num) for num in line.split()]
                self._tiles.append(row)

    @property
    def tiles(self):
        return self._tiles

    def place_entity(self, entity_id: int, x: int, y: int):
        self._tiles[y][x] = entity_id

    def reset_tile(self, x: int, y: int):
        self._tiles[y][x] = 49  # I set 49 as the default tile

    def __repr__(self):
        buffer = [
            "Active Map Contents:\n",
            "       00     01     02     03     04     05     06     07     08"
            "     09     10     11     12     13     14     15  \n"
        ]
        for index, row in enumerate(self._tiles):
            buffer.append(f"{index:02}  ")
            buffer.extend([f"|  {element:02}  " for element in row])
            buffer.append("|\n")
        buffer.append(
            "       00     01     02     03     04     05     06     07     08"
            "     09     10     11     12     13     14     15  \n"
        )
        return "".join(buffer)
