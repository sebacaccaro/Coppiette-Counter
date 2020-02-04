from telegram.ext import Updater, CommandHandler
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Usa /cpp per aggiungere una coppietta. Usa /ncpp per segnalare che non hai trovato coppiette")


def addCoppietta(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Ho aggiunto una nuova coppietta!"
    )


def noCoppietta(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Ottimo, nessuna coppietta oggi!"
    )


updater = Updater(
    token='LOL', use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
add_handler = CommandHandler('cpp', addCoppietta)
noc_handler = CommandHandler('ncpp', noCoppietta)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(noc_handler)
updater.start_polling()
