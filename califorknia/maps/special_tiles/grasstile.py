import califorknia.logger as logger

from califorknia.maps.tile import Tile

log = logger.get_logger(__name__)


class GrassTile(Tile):

    def __init__(self, tile_id: int = 10):
        self._id = tile_id
        super().__init__(tile_id)

    def on_player_walk(self):
        super().on_player_walk()
        log.info('Combat initiated!')




