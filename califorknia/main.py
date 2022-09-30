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

WINDOW_NAME = "Califorknia"
WIDTH = 800
HEIGHT = 600
FPS = 60

log = logger.get_logger(__name__)
log.info("Logger loaded.")


def main() -> None:
    log.info("Script entry point.")
    pygame.init()
    pygame.display.set_caption(WINDOW_NAME)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game_running = True
    while game_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        screen.fill((255, 255, 255))
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    # log.info("Starting up!")
    main()
    logger.shutdown_logger()
