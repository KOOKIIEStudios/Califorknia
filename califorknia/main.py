"""This module is the entry point for the program.

Califorknia is a simple PyGame-based RPG game.
In this game, foodstuffs have come alive following the alien invasion of
Califorknia, and your job is to tame them and use them to defeat the aliens and
liberate Califorknia.

    Typical usage example:

    python califorknia/main.py
"""
import logger
import pygame

from califorknia.constants import *
from califorknia.entities.player import Player
from califorknia.map.map import Map

log = logger.get_logger(__name__)
log.info("Logger loaded.")


def main() -> None:
    log.info("Script entry point.")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    orange_county = Map(screen)
    player = Player("Player", map_=orange_county, pos=(0, 0))
    orange_county.place_entity(player, 10, 5)
    pygame.init()
    pygame.display.set_caption(WINDOW_NAME)
    clock = pygame.time.Clock()
    game_running = True
    while game_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        player.listen_input()
        screen.fill((0, 0, 0))
        orange_county.render_map()
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    # log.info("Starting up!")
    main()
    logger.shutdown_logger()
