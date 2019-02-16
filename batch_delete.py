import tweepy
from credentials import *


def batch_delete(api):
    print("You are about to Delete all tweets from the account @%s." % api.verify_credentials().screen_name)
    print("Does this sound ok? There is no undo! Type yes to carry out this action.")
    do_delete = input("> ")
    if do_delete.lower() == 'yes':
        for status in tweepy.Cursor(api.user_timeline).items():
            try:
                api.destroy_status(status.id)
                print("Deleted:", status.id)
            except:
                print("Failed to delete:", status.id)


auth = tweepy.OAuthHandler(CONSUMER_KEY,
                           CONSUMER_SECRET)  # Twitter requires all requests to use OAuth for authentication
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

batch_delete(api)
