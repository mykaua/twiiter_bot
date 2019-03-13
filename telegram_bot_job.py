from telegram.ext import Updater, CommandHandler, Job, MessageHandler, Filters, InlineQueryHandler
import sys
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

INTERVAL = 60 #15 mins
TOKEN = 'xxxx'

def message_to_telegram(bot, job):
    bot.sendMessage(chat_id=job.context, text='https://t.co/WHkDi91Fti')

#-------------------------------------
def start(bot, update, job_queue):
    chat_id = update.message.chat_id
    bot.sendMessage(update.message.chat_id, text="Hello world")
    job = job_queue.run_repeating(message_to_telegram, INTERVAL, first=5, context=update.message.chat_id) # message every 60 second

def help_handler(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, text='Fuck you!:)')

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def startTelegramBot():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start, pass_job_queue=True))
    dp.add_handler(CommandHandler("help", help_handler))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

def main():
    startTelegramBot()

if __name__ == '__main__':
    main()
