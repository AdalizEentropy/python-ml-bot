import json
import logging
import os
import random

INTENTS_FILE_NAME = "templates/big_bot_config.json"
intents = {}
failure_phrases = {}


def load_intents():
    global intents, failure_phrases
    if os.path.exists(INTENTS_FILE_NAME) and os.path.getsize(INTENTS_FILE_NAME) != 0:
        with open(INTENTS_FILE_NAME, "r") as file:
            data = json.load(file)
            intents = data["intents"]
            failure_phrases = data["failure_phrases"]
            logging.debug("Intents were loaded from file: %s", len(intents))
    else:
        logging.info("There no intents data for loading")
    return intents


def get_intents():
    return intents


def get_random_response(intent):
    if intent == "failure_phrases":
        return random.choice(failure_phrases)
    else:
        return random.choice(intents[intent]["responses"])
