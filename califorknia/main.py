"""This module is the entry point for the program.

Califorknia is a simple PyGame-based RPG game.
In this game, foodstuffs have come alive following the alien invasion of
Califorknia, and your job is to tame them and use them to defeat the aliens and
liberate Califorknia.

    Typical usage example:

    python califorknia/main.py
"""
import listener
import logger
import pygame

from califorknia.constants.constants import *
import constants.events as events
from constants.direction import Direction
from world import World

log = logger.get_logger(__name__)
log.info("Logger loaded.")


def main() -> None:
    log.info("Script entry point.")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    world = World(screen)

    pygame.init()
    pygame.display.set_caption(WINDOW_NAME)
    clock = pygame.time.Clock()
    pygame.time.set_timer(events.AUTO_SAVE, 600000)  # 10 min

    game_running = True
    while game_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            # log.debug(event.type)
            match event.type:
                case pygame.QUIT:
                    game_running = False

                case events.MOVE_UP.type:
                    world.move_player(Direction.UP)
                case events.MOVE_DOWN.type:
                    world.move_player(Direction.DOWN)
                case events.MOVE_LEFT.type:
                    world.move_player(Direction.LEFT)
                case events.MOVE_RIGHT.type:
                    world.move_player(Direction.RIGHT)

            if listener.is_pause_toggled(event):
                pass
            if listener.is_menu_toggled(event):
                pass
            if listener.is_start_running(event):
                world.start_player_run()
            if listener.is_stop_running(event):
                world.stop_player_run()

        listener.listen_input()
        screen.fill((0, 0, 0))
        world.render_map()
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    # log.info("Starting up!")
    main()
    logger.shutdown_logger()
