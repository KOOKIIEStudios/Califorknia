import logger


log = logger.get_logger(__name__)
log.info("Logger loaded.")


def main() -> None:
    log.info("Scipt entry point.")


if __name__ == "__main__":
    # log.info("Starting up!")
    main()
    logger.shutdown_logger()
