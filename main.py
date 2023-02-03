from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from settings import *
import requests

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text('WikiPedia Botga xush kelibisz!!!\n'
                              'Sorovingizni /search komandasi orqali kiriting kiriting.')


def search(update: Update, context: CallbackContext):
    words = context.args
    if len(words) == 0:
        update.message.reply_text("Hech bolmasa /search komandasidan keyin nimadir kiriting !!")
    else:
        search_word = ' '.join(words)
        result = requests.get('https://uz.wikipedia.org/w/api.php', {
            'action': 'opensearch',
            'search': search_word,
            'limit': 1,
            'namespace': 0,
            'format': 'json'
        })
        result = result.json()
        wiki_link = result[3]
        if len(wiki_link):
            update.message.reply_text("So'rovingiz bo'yicha quyidagi link topildi\n"
                                      + wiki_link[0])
        else:
            update.message.reply_text("Hechnima topilmadi!!")


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))
dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=start))
updater.start_polling()
updater.idle()
