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
from constants import events
from constants.direction import Direction
from world import World

log = logger.get_logger(__name__)
log.info("Logger loaded.")


def main() -> None:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    world = World(screen)

    pygame.init()
    pygame.display.set_caption(WINDOW_NAME)
    clock = pygame.time.Clock()
    pygame.time.set_timer(events.AUTO_SAVE, 600000)  # 10 min

    game_running = True
    log.info("PyGame loaded. Start running game.")
    while game_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            # log.debug(event.type)
            match event.type:
                case pygame.QUIT:
                    game_running = False
                    log.warning("Quit event encountered.")

                case events.MOVE_UP.type:
                    world.move_player(Direction.UP)
                case events.MOVE_DOWN.type:
                    world.move_player(Direction.DOWN)
                case events.MOVE_LEFT.type:
                    world.move_player(Direction.LEFT)
                case events.MOVE_RIGHT.type:
                    world.move_player(Direction.RIGHT)

                case events.AUTO_SAVE.type:
                    log.debug("Progress has been automatically saved.")
                    pass  # TODO: Auto-save function

            if listener.is_pause_toggled(event):
                log.debug("Game paused")
                pass  # TODO: Make it possible to pause the game
                # Pausing should bring up a dialogue with option to quit/save
            if listener.is_menu_toggled(event):
                log.debug("Menu toggled open/close")
                pass  # TODO: Open player menu for inventory
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
    exit("End of Script Reached")
