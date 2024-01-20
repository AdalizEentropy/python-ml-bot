import logging
import logging.config
import os

import yaml

import storage
import ml

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
    ml.modeling(intents)
    while True:
        print(">> ")
        _input = input()
        intent = ml.get_intent(_input)
        logging.info("Intent: %s, Response: %s", intent, storage.get_random_response(intent))


if __name__ == "__main__":
    main()
