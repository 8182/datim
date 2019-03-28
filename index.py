#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import requests

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

url = "https://api.wolframalpha.com/v1/result?i="
appid = "xxx"

def start(bot, update):
    update.message.reply_text('Hi!')


def help(bot, update):
    update.message.reply_text('Help!')

# query https://api.wolframalpha.com/v1/result?i=time+until+next+sunday%3F&appid=xxx

def answer(bot, update):
    query = update.message.text
    req = requests.get("{0}{1}&appid={2}".format(url, query, appid))
    update.message.reply_text(req.text)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater("xxx")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, answer))
    dp.add_error_handler(error)
    updater.start_polling()
    logger.info("Ready to rock..!")
    updater.idle()


if __name__ == '__main__':
    main()
