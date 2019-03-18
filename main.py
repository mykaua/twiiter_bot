from telegram.ext import Updater, CommandHandler, Job, MessageHandler, Filters, InlineQueryHandler
import sys
import logging
import requests
import re
import twitter
import twitter_tokens
import logging
import datetime

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


twitter_user = twitter_tokens.twitter_user
telegram_token = twitter_tokens.telegram_token
INTERVAL = 1800

api = twitter.Api(twitter_tokens.consumer_key,
                  twitter_tokens.consumer_secret,
                  twitter_tokens.access_token_key,
                  twitter_tokens.access_token_secret
                  )
#-----------TWITTER API -----------#
#---- last tweet -----#
def take_last_tweet():
    statuses = api.GetUserTimeline(screen_name=twitter_user)
    tweet = statuses[0].text.encode('utf-8')
    return tweet

#----- write to file ---#
def write_to_file( tweet ):
    file = open("tweet.txt", "w")
    file.write(str(tweet))
    file.close

#----- read from file -----#
def read_from_file():
    file = open("tweet.txt", "r")
    first_line = file.readline()
    return first_line




#--- check differnt between last tweets ---#
def message_to_telegram(bot, job):
    tweet = take_last_tweet()
    read_tweet_file = read_from_file()
    if read_tweet_file != str(tweet):
        bot.sendMessage(chat_id=job.context, text=tweet, disable_notification=True)
        write_to_file(tweet)
    else:
        print ("tweet same" + datetime.datetime.now())
#--------TELEGRAM API ------#

#def message_to_telegram(bot, job):
#    bot.sendMessage(chat_id=job.context, text='https://t.co/WHkDi91Fti')

#-------------------------------------
def start(bot, update, job_queue):
    chat_id = update.message.chat_id
    bot.sendMessage(update.message.chat_id, text="Hello world")
    job = job_queue.run_repeating(message_to_telegram, INTERVAL, first=5, context=update.message.chat_id) # message every 60 second

def help_handler(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, text='Fuck you, asshole!:)')

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def startTelegramBot():
    updater = Updater(telegram_token)
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
