# KaomojiRobot

import logging, os
from kaomoji import Kaomoji
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, InlineQueryHandler

# Environment Variables
BOT_TOKEN = os.environ['BOT_TOKEN']


# Logging
logging.basicConfig(filename=os.getcwd() + '/error_bot.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

log = logging.getLogger(__name__)


def errorlog(update, context):
    log.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    kaomoji = Kaomoji(BOT_TOKEN)

    update = Updater(token=kaomoji.token, use_context=True)

    dispatch = update.dispatcher

    dispatch.add_handler(InlineQueryHandler(kaomoji.inlinequery))

    # Logging for errors
    dispatch.add_error_handler(errorlog)

    # start the bot
    update.start_polling()

    # Block until user presses CTRL-C
    update.idle()


if __name__ == '__main__':
    main()
