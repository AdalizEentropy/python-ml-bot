import logging
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters

import bot

TOKEN = os.environ['PYTHON_ML_BOT_TOKEN']
app = ApplicationBuilder().token(TOKEN).build()


async def telegram_reply(upd: Update, ctx):
    name = upd.message.from_user.full_name
    user_text = upd.message.text
    logging.debug("Message received: user '%s', message '%s'", name, user_text)
    reply = bot.get_answer(name, user_text)
    logging.debug("Message send: user '%s', message '%s'", name, reply)
    await upd.message.reply_text(reply)


def run_telegram_bot():
    handler = MessageHandler(filters.TEXT, telegram_reply)
    app.add_handler(handler)
    app.run_polling()
