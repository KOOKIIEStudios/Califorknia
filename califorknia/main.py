"""This module is the entry point for the program.

Califorknia is a simple PyGame-based RPG game.
In this game, foodstuffs have come alive following the alien invasion of
Califorknia, and your job is to tame them and use them to defeat the aliens and
liberate Califorknia.

    Typical usage example:

    python califorknia/main.py
"""
import logger


log = logger.get_logger(__name__)
log.info("Logger loaded.")


def main() -> None:
    log.info("Script entry point.")


if __name__ == "__main__":
    # log.info("Starting up!")
    main()
    logger.shutdown_logger()
