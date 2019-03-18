docker build .

docker run -ti -d -e consumer_key=key \                               
-e consumer_secret=key \
-e access_token_key=key \
-e access_token_secret=key \
-e twitter_user=@twitter_user \
-e telegram_token=key \
image
