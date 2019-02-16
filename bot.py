import re
from os import environ

import tweepy

from cardcreator import render_card
from resources.exceptions import *
from resources.player import Player

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY,
                           CONSUMER_SECRET)  # Twitter requires all requests to use OAuth for authentication
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

'''
PATTERN is in the form '[Name,Position,Club,Country,Overall,PAC,DRI,SHO,DEF,PAS,PHY,CARD_CODE,LANGUAGE_CODE]'
- there is an optional space allowed after each comma in the list
- LANGUAGE_CODE is optional

Examples:
1) re will match [Messi,RW,241,AR,94,92,95,88,24,86,62,IF_GOLD]
2) re will match [Messi, RW, 241, AR, 94, 92, 95, 88, 24, 86, 62, IF_GOLD]
3) re will match [Messi, RW, 241, AR, 94, 92, 95, 88, 24, 86, 62, IF_GOLD, ES]
'''

p = re.compile(
    r'\[[a-zA-Z ]{1,17},[ ]?'
    r'[a-zA-Z]{2,3},[ ]?\d{1,10},[ ]?[a-zA-Z]{1,3},[ ]?'
    r'\d{1,2},[ ]?'
    r'\d{1,2},[ ]?\d{1,2},[ ]?'
    r'\d{1,2},[ ]?\d{1,2},[ ]?'
    r'\d{1,2},[ ]?\d{1,2},[ ]?'
    r'[a-zA-Z_]{1,20}'
    r'(,[ ]?[a-zA-Z]{2})?\]',
    re.IGNORECASE | re.VERBOSE)


# create a class inheriting from the tweepy  StreamListener
class BotStreamer(tweepy.StreamListener):
    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        tweet_text = status.text

        if hasattr(status, 'retweeted_status'):
            return

        params = re.search(p, tweet_text)

        if not params:
            return

        parameters = params.group()[1:-1].split(',')

        name = parameters[0].strip()
        position = parameters[1].strip()
        club = parameters[2].strip()
        country = parameters[3].strip()
        overall = parameters[4].strip()
        pac = parameters[5].strip()
        dri = parameters[6].strip()
        sho = parameters[7].strip()
        deff = parameters[8].strip()
        pas = parameters[9].strip()
        phy = parameters[10].strip()
        card_code = parameters[11].strip()

        # attempt to get the optional language code
        try:
            lang_code = parameters[12].strip().upper()
        except IndexError:
            lang_code = 'EN'

        if 'media' in status.entities and status.entities['media'][0]['type'] == 'photo':
            image_url = status.entities['media'][0]['media_url']
        else:
            image_url = None

        try:
            player = Player(name, position, club, country, overall, pac, dri, sho, deff, pas, phy, lang_code)
            path_to_card_img = render_card(player, card_code, image_url, status.id)
        except FileNotFoundError as err:
            return
        except InvalidCardCodeError:
            return
        except InvalidCountryCodeError:
            return
        except InvalidClubNumberError:
            return
        except InvalidPositionError:
            return
        except InvalidLanguageError:
            return

        api.update_with_media(path_to_card_img, status='@{}'.format(username), in_reply_to_status_id=status.id)


myStreamListener = BotStreamer()
# Construct the Stream instance
stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=['@futcardcreator'])
