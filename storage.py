import json
import os
import logging

INTENTS_FILE_NAME = "templates/big_bot_config.json"
intents = {}


def load_intents():
    if os.path.exists(INTENTS_FILE_NAME) and os.path.getsize(INTENTS_FILE_NAME) != 0:
        with open(INTENTS_FILE_NAME, "r") as file:
            data = json.load(file)
            for examples, responses in data["intents"].items():
                intents[examples] = responses
            logging.debug("Intents were loaded from file: %s", len(intents))
    else:
        logging.info("There no intents data for loading")
    return intents


def get_intents():
    return intents