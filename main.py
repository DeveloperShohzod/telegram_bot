from telegram import Update
from telegram.ext import Updater, CallbackContext,CommandHandler

updater = Updater(token="6077702907:AAGaVvvJ6EAkVWSFWC9X-3EJn8nWi7ulQeg", use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello New Bot')


dispatcher = updater.dispatcher
add_handler = dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
