import requests
import re
import twitter
import twitter_tokens


twitter_user = twitter_tokens.twitter_user

api = twitter.Api(twitter_tokens.consumer_key,
                  twitter_tokens.consumer_secret,
                  twitter_tokens.access_token_key,
                  twitter_tokens.access_token_secret
                  )

#---- last tweet -----#
def take_last_tweet():
    statuses = api.GetUserTimeline(screen_name=twitter_user)
    tweet = statuses[0].id
    return tweet
#--- check differnt between last tweets ---#
def differnt_beetween_tweets ():
    tweet = take_last_tweet()
    read_tweet_file = read_from_file()
    if read_tweet_file != str(tweet):
        print "tweet differnt"
        write_to_file(tweet)
    else:
        print "tweet same"

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

def main():
    differnt_beetween_tweets()

if __name__ == '__main__':
    main()
