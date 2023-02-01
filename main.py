from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler
from settings import *

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello New Bot')


dispatcher = updater.dispatcher
add_handler = dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
