from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler
import requests
import re
import twitter
import twitter_tokens
import csv

twitter_user_id = twitter_tokens.twitter_user_id
twitter_user = twitter_tokens.twitter_user

api = twitter.Api(twitter_tokens.consumer_key,
                  twitter_tokens.consumer_secret,
                  twitter_tokens.access_token_key,
                  twitter_tokens.access_token_secret
                  )

#---- last tweet -----#
def take_last_tweet():
    statuses = api.GetUserTimeline(screen_name=twitter_user)
    tweet = statuses[0].text.encode('utf-8')
#    if statuses[0].text != statuses[1].text:
#        print statuses[0].text
        #tweet = statuses[0].text
#    write_to_file(tweet)
    return tweet
#    read = read_from_file()
#    if read != tweet:
#        print tweet
#        write_to_file(tweet)
#    else
#        print "hello world"

def differnt ():
    tweet = take_last_tweet()
    read = read_from_file()
    print read
    print "------"
    print tweet
    print "-------"
    if read != str(tweet):
        print "tweet"
        write_to_file(tweet)
    else:
        print "hello world"
#    checking(arg1=read, arg2=tweet)

#print take_last_tweet()
#----- STream tweets -----#
#def tweets():
#    stream = api.GetStreamFilter(follow=[twitter_user_id])
#    for s in stream:
#        tweet = twitter.Status.NewFromJsonDict(s)
#        tsi = tweet.text
#        print tsi
#        print tweet.id

#last_tweet = take_last_tweet()
#print last_tweet
#def tweets():
#    tweets = list(api.GetUserTimeline(screen_name=twitter_user))
#    tweet = tweets[0].id

#print tweets
#print (type(tweets))
#print (len(tweets))
#print tweets[0].id
#print tweets[1].id
#print "-------"
#if tweets[0].id != tweets[1].id:
#    print tweets[0].text
#print "---------"
#for tweet in tweets:
#    print tweet.id
#    if tweet[0].id != tweet[1].id:
#        print tweet[0].id
#def file (tweet):
#file = open("1.csv", "w+")
#file.write(str(tweets[0].id))
#file.close

#file1 = open("1.csv", "r")
#f1 = file1.readline()
#print f1
#file1.close

def write_to_file( tweet ):
    file = open("tweet.txt", "w")
    file.write(str(tweet))
    file.close

def read_from_file():

    file = open("tweet.txt", "r")
    first_line = file.readline()
    return first_line

def main():
#    take_last_tweet()
#    write_to_file()
#    read_from_file()
    differnt()


if __name__ == '__main__':
    main()
