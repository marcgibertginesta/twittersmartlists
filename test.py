#!/usr/bin/python

# print "Halt!"
# user_reply = raw_input("Who goes there? ")
# print "You may pass,", user_reply

#from twitter import *
#import os

import twitter
from twitter.oauth_dance import oauth_dance
import json
import os
import pprint

#import webbrowser

SCREEN_NAME = "marcgibert"
CONSUMER_KEY = "GV0LKJYkEI1Py2oJ0vbITQ" # consumer key
CONSUMER_SECRET = "bKNnKLNn1i5nTP9rnqj3OK5SGHx5PHF4m2hekLe28" # consumer secret

MY_TWITTER_CREDS = os.path.expanduser('~/.my_app_credentials')
if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance("MGSmartLists", CONSUMER_KEY, CONSUMER_SECRET,
                MY_TWITTER_CREDS)

oauth_token, oauth_secret = twitter.read_token_file(MY_TWITTER_CREDS)

#(oauth_token, oauth_token_secret) = oauth_dance('MGSmartLists',
#        CONSUMER_KEY, CONSUMER_SECRET)

#t = twitter.Twitter(domain='api.twitter.com', api_version='1.1',
#                    auth=twitter.oauth.OAuth(oauth_token, oauth_token_secret,
#                    CONSUMER_KEY, CONSUMER_SECRET))

t = twitter.Twitter(auth=twitter.OAuth(
    oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))


#twitterConnect = twitter.Twitter(auth=twitter.oauth.OAuth('', '', app_key, app_secret), format='')
#oauth_token, oauth_token_secret = twitter.oauth_dance.parse_oauth_tokens(twitterConnect.oauth.request_token())
#oauth_url = ('http://api.twitter.com/oauth/authorize?oauth_token=' + oauth_token)
 
#webbrowser.open(oauth_url)

#t = Twitter(
#            auth=OAuth("19880799-2v13ExCgQDWinIPDBlxAhFLunff6GzVnr0jjoHHQV", "mcSpKfc9Evsw6V2ORsuO1ZbRPjuKZKXoUESLsFG0GYgCL",
#                       "GV0LKJYkEI1Py2oJ0vbITQ", "bKNnKLNn1i5nTP9rnqj3OK5SGHx5PHF4m2hekLe28")
#           )

#oauth_verifier = raw_input("Twitter PIN: ")
#twitterConnect = twitter.Twitter(auth=twitter.oauth.OAuth(oauth_token, oauth_token_secret, app_key, app_secret), format='')
#oauth_token, oauth_token_secret = twitter.oauth_dance.parse_oauth_tokens(twitterConnect.oauth.access_token(oauth_verifier=oauth_verifier))

# Get your "home" timeline
#t.statuses.home_timeline()
#t.statuses.friends_timeline(id="19880799")
#

cursor = -1
ids = []

response = t.friends.ids(screen_name=SCREEN_NAME, cursor=cursor)
ids.extend(response['ids'])
print ids

response = t.statuses.mentions_timeline(count=-1)
print json.dumps(response, indent=4, sort_keys=True)


#t.statuses.home_timeline(count=5)