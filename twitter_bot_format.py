import twitter
import twitter_tokens

twitter_user_id = twitter_tokens.twitter_user_id

api = twitter.Api(twitter_tokens.consumer_key,
                  twitter_tokens.consumer_secret,
                  twitter_tokens.access_token_key,
                  twitter_tokens.access_token_secret
                  )

def tweets():
    stream = api.GetStreamFilter(follow=[twitter_user_id])
    for s in stream:
        tweet = twitter.Status.NewFromJsonDict(s)
        tsi = tweet=tweet.text
        print tsi

latest_tweets = tweets()
print latest_tweets
