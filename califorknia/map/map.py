"""
    Map will be grid-based and will be a 2D array of tiles.
    [ [] [] [] [] []
      [] [] [] [] []
      [] [] [] [] [] ]
"""
from califorknia.constants import TILE_SIZE, WIDTH, HEIGHT


class Map:
    _tiles: list[list] = []
    _window = None

    def __init__(self, window):
        self._window = window
        self.init_tiles()

    def init_tiles(self):
        row = [0 for _ in range(WIDTH // TILE_SIZE)]
        self._tiles = [row for _ in range(HEIGHT // TILE_SIZE)]
        print(self._tiles)

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
