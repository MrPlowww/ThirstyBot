"""Configures Twitter API for use with Twitter Account credentials, as passed into the function via
JSON-formatted object 'twitter_credentials', which must include key:values for these keys:
    'consumer_key'
    'consumer_secret'
    'access_token'
    'access_token_secret'
"""
def init_twitter_api(twitter_credentials): # 'credentials' is a string-formatted location/json file
    import tweepy  # import tweepy Twitter API
    auth = tweepy.OAuthHandler(twitter_credentials['consumer_key'],
                               twitter_credentials['consumer_secret'])
    auth.set_access_token(twitter_credentials['access_token'],
                          twitter_credentials['access_token_secret'])
    return tweepy.API(auth)