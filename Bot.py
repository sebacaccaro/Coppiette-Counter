from telegram.ext import Updater, CommandHandler
from SheetsModule import addCoppietta as add, noCpp
import logging


def getToken():
    with open("../token.txt") as tokenFile:
        return str.strip(tokenFile.readline())


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Usa /cpp per aggiungere una coppietta. Usa /ncpp per segnalare che non hai trovato coppiette")


def addCoppietta(update, context):
    res = add()
    message = "Ahia, cominciamo male! Prima coppietta!" if res == 1 else "Coppietta numero {} di oggi".format(
        res)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=message
    )


def noCoppietta(update, context):
    res = noCpp()
    message = "Ottimo, per ora todo bien" if res != -1 \
        else "Vecchio, ne hai già segnata almeno una prima"
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=message
    )


updater = Updater(
    token=getToken(), use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
add_handler = CommandHandler('cpp', addCoppietta)
noc_handler = CommandHandler('ncpp', noCoppietta)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(noc_handler)
updater.start_polling()
