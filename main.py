import logging
import logging.config
import os
import telegram_bot

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


if __name__ == "__main__":
    get_logger()
    intents = storage.load_intents()
    ml.modeling(intents)
    telegram_bot.run_telegram_bot()
