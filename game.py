#!/usr/bin/env python
import json
import twitter
import time

# HackPittsburh's Tar and Feather game
#  Requires the python-twitter libary from https://github.com/bear/python-twitter

SEARCH_STRING = '@HackPGH'

config_file = open('auth.json', 'r')
config = json.load(config_file)

api = twitter.Api(consumer_key = config['consumer_key'],
                  consumer_secret = config['consumer_secret'],
                  access_token_key = config['access_token_key'],
                  access_token_secret = config['access_token_secret'])

def run_game():
    last_id = api.GetSearch(term = SEARCH_STRING, count = 1)[0].id

    print "Starting new game."
    time.sleep(60)

    tweets = api.GetSearch(term = SEARCH_STRING, since_id = last_id, count = 100)
    for item in tweets:
        tweet = item.AsDict()
        print tweet['user']['screen_name'], '->', tweet['text']

while True:
    run_game()
