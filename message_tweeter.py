""" Message Tweeter: This module uses the Twitter API (via Python package 'tweepy') to tweet the output of module
# 'message_generator.py'.
# 0.0) Prerequisites
#      0.1) Python Dependencies:
#           0.1.1) Python module 'message_generator.py' shall be Python path-accessible.
#           0.2.2) Python package 'tweepy' shall be installed into the active Python environment.
#      0.2) Configuration Dependencies:
#           0.2.a) Twitter: The target Twitter account shall be properly configured for Twitter API access.
#           0.2.b) Twitter: The calling module shall have already initialized the Twitter API (with the proper
#                  Twitter account credentials) via module 'init_twitter_api.py', and shall pass that API to this
#                   module via the 'api' object (i.e., that calling module must execute
#                  'api = init_twitter_api.init_twitter_api(twitter_credentials)' (where 'twitter_credentials' is the
#                   JSON-formatted file containing the secret Twitter account keys), and then passed 'api' on to this
#                   module for subsequent use).
# 1.0) Run-time notes:
#   1.1) Usage:
#       1.1.1) standalone?: No.
#       1.1.2) call from another module?: Yes, by doing the following from the calling module:
#            >>> import message_tweeter
#            >>> message_tweeter.lets_tweet_message(api)  # must pass the api object into this module.
# 2.0) Changelog:
#       Version 1.0: Original version.
"""

import message_generator
from time import strftime


def lets_tweet_message(api):  # Live-tweet a random message
    try:
        words = message_generator.define_words()  # Initializes the word dictionary.
        all_jobs = message_generator.message(words)  # Builds list of jobs (w/o preable) from random words in word dictionary
        message = message_generator.respond_one(all_jobs)  # Returns a single randomly chosen message from the message list (with default reamble) and store it in "message"
        api.update_status(status=message)    # tweet random message stored in "message"; disable this line to prevent actual tweeting (but all other code will execute)
        print(strftime("%Y-%m-%d %H:%M:%S") + ' - tweeted: ' + str(message))
        pass
    except tweepy.error.TweepError:
        print(strftime("%Y-%m-%d %H:%M:%S") + ' - TweepError prevented message tweet')
        pass