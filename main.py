import logging
import logging.config
import storage
import yaml
import os

LOGGER_FILE = "templates/logging.yml"


def get_logger():
    if os.path.exists(LOGGER_FILE) and os.path.getsize(LOGGER_FILE) != 0:
        with open(LOGGER_FILE, "r") as file:
            logging_config = yaml.safe_load(file)
            logging.config.dictConfig(logging_config)
            logging.warning("Log level was set to %s", logging.getLevelName(logging.getLogger().level))


def main():
    get_logger()
    intents = storage.load_intents()


if __name__ == "__main__":
    main()



