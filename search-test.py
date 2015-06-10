#!/usr/bin/env python
import json
import twitter

# Search twitter for recent posts
#  Requires the python-twitter libary from https://github.com/bear/python-twitter

SEARCH_STRING = '@HackPGH'

config_file = open('auth.json', 'r')
config = json.load(config_file)

api = twitter.Api(consumer_key = config['consumer_key'],
                  consumer_secret = config['consumer_secret'],
                  access_token_key = config['access_token_key'],
                  access_token_secret = config['access_token_secret'])

for status in api.GetSearch(SEARCH_STRING):
    item = status.AsDict()
    print item['user'] ['screen_name'], '->', item['text']
