#!/usr/bin/env python
import json
import twitter
import time

# HackPittsburh's Tar and Feather game
#  Requires the python-twitter libary from https://github.com/bear/python-twitter

class WhiskeyGame():
    def __init__(self):
        self.SEARCH_STRING = '@HackPGH'
        self.config_file = open('auth.json', 'r')
        self.config = json.load(self.config_file)
        self.api = twitter.Api(consumer_key = self.config['consumer_key'],
                               consumer_secret = self.config['consumer_secret'],
                               access_token_key = self.config['access_token_key'],
                               access_token_secret = self.config['access_token_secret'])
        self.last_id = self.api.GetSearch(term = self.SEARCH_STRING, count = 1)[0].id
        self.taxes_tally = 0 
        self.whiskey_tally = 0
        self.tax_tweets = []
        self.whiskey_tweets = []
    
    def run_game(self):
        tweets = self.api.GetSearch(term = self.SEARCH_STRING, since_id = self.last_id, count = 100)
        for item in tweets:
            tweet = item.AsDict()
            tweetstring = tweet['user']['screen_name'] + '->' + tweet['text']
            print tweetstring
            text = tweet['text'].lower()
            if "@wiglewhiskey" in text:
                if "#taxes" in text or "#tax" in text:
                    print "Found vote for #taxes."
                    self.taxes_tally += 1
                    self.tax_tweets.append(tweetstring)
                if "#whiskey" in text or "#whisky" in text:
                    print "Found vote for #whiskey."
                    self.whiskey_tally += 1
                    self.whiskey_tweets.append(tweetstring)
            if item.id > self.last_id:
                self.last_id = item.id
    
    def start(self):
        countdown = 120
        sleepdelay = 5
        while (countdown > 0):
            print "Polling, {0} seconds left...".format(countdown)
            self.run_game()
            print "   {0} votes for taxes.".format(self.taxes_tally)
            for tweet in self.tax_tweets:
                print "      " + tweet
            print "   {0} votes for whiskey.".format(self.whiskey_tally)
            for tweet in self.whiskey_tweets:
                print "      " + tweet
            time.sleep(sleepdelay)
            countdown -= sleepdelay
        
        print "GAME OVER"
        print "Taxes:   {0} votes.".format(self.taxes_tally)
        print "Whiskey: {0} votes.".format(self.whiskey_tally)

print "Starting new game."
whiskey_game = WhiskeyGame()
whiskey_game.start()
