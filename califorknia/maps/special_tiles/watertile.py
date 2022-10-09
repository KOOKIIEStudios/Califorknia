import califorknia.logger as logger

from califorknia.maps.tile import Tile

log = logger.get_logger(__name__)


class WaterTile(Tile):

    def __init__(self, tile_id: int = 11):
        self._id = tile_id
        super().__init__(tile_id, traversable=False)

    def on_player_walk(self):
        super().on_player_walk()
        log.warning('Player should not walk on water.')






