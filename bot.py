from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import datetime

def start(update: Update, context: CallbackContext) -> None:
    """Invia un messaggio quando il comando /start è invocato."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Ciao {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def data_odierna(update: Update, context: CallbackContext) -> None:
    oggi = datetime.date.today()
    update.message.reply_text("La data odierna è: " + str(oggi))

def aggiungi_giorni(update: Update, context: CallbackContext) -> None:
    # Ottiene argomenti passati al comando
    args = context.args

    if len(args) != 2:
        update.message.reply_text('Usage: /aggiungi AAAA-MM-GG giorni')
        return

    data = args[0]
    giorni = int(args[1])
    data_modificata = datetime.datetime.strptime(data, '%Y-%m-%d').date() + datetime.timedelta(days=giorni)
    update.message.reply_text("La nuova data è: " + str(data_modificata))

def sottrai_giorni(update: Update, context: CallbackContext) -> None:
    # Ottiene argomenti passati al comando
    args = context.args

    if len(args) != 2:
        update.message.reply_text('Usage: /sottrai AAAA-MM-GG giorni')
        return

    data = args[0]
    giorni = int(args[1])
    data_modificata = datetime.datetime.strptime(data, '%Y-%m-%d').date() - datetime.timedelta(days=giorni)
    update.message.reply_text("La nuova data è: " + str(data_modificata))

def main() -> None:
    """Start the bot."""
    # Crea l'Updater e passa il tuo token del bot.
    updater = Updater("TOKEN", use_context=True)

    # Ottieni il dispatcher per registrare i gestori
    dispatcher = updater.dispatcher

    # su diversi comandi - in questo caso, start, aggiungi e sottrai
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("data_odierna", data_odierna))
    dispatcher.add_handler(CommandHandler("aggiungi", aggiungi_giorni))
    dispatcher.add_handler(CommandHandler("sottrai", sottrai_giorni))

    # Avvia il Bot
    updater.start_polling()

    # Esegui il bot fino a quando non viene inviato il comando Ctrl-C o il processo riceve SIGINT,
    # SIGTERM o SIGABRT. Questo dovrebbe essere usato per la maggior parte dei casi, poiché
    # start_polling() non è bloccante e arresta il bot con grazia.
    updater.idle()


if __name__ == '__main__':
    main()
