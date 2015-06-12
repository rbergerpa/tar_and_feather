#!/usr/bin/env python
import json
import twitter
import time
from dunk import Dunk

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
        self.dunk = Dunk()
        self.reset_game()

    def reset_game(self):
        self.taxes_tally = 0 
        self.whiskey_tally = 0
        self.tax_tweets = []
        self.whiskey_tweets = []
        self.dunk.reset_switches()
        self.last_id = self.api.GetSearch(term = self.SEARCH_STRING, count = 1)[0].id
        
    def run_game(self):
        tweets = self.api.GetSearch(term = self.SEARCH_STRING, since_id = self.last_id, count = 100)
        for item in tweets:
            tweet = item.AsDict()
            tweetstring = tweet['user']['screen_name'] + '->' + tweet['text']
            print tweetstring
            text = tweet['text'].lower()
# too many people are going to mis-spell this, so...
#            if "@wiglewhiskey" in text:
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

    def confirm(self, prompt=None, resp=False):
        """prompts for yes or no response from the user. Returns True for yes and
        False for no.

        'resp' should be set to the default value assumed by the caller when
        user simply types ENTER.

        >>> confirm(prompt='Create Directory?', resp=True)
        Create Directory? [y]|n: 
        True
        >>> confirm(prompt='Create Directory?', resp=False)
        Create Directory? [n]|y: 
        False
        >>> confirm(prompt='Create Directory?', resp=False)
        Create Directory? [n]|y: y
        True
        
        """
    
        if prompt is None:
            prompt = 'Confirm'

        if resp:
            prompt = '%s [%s]|%s: ' % (prompt, 'y', 'n')
        else:
            prompt = '%s [%s]|%s: ' % (prompt, 'n', 'y')
                
        while True:
            ans = raw_input(prompt)
            if not ans:
                return resp
            if ans not in ['y', 'Y', 'n', 'N']:
                print 'please enter y or n.'
                continue
            if ans == 'y' or ans == 'Y':
                return True
            if ans == 'n' or ans == 'N':
                return False

    def game_loop(self):
        # Note, user resource limit is 180 requests every 15 minutes, 
        # which works out to 1 request every 5 seconds MAX
        # Setting to 1 request every 6 seconds for a good safety margin
        countdown = 120
        sleepdelay = 10
        while (countdown > 0):
            print "Polling, {0} seconds left...".format(countdown)
            self.run_game()
            print "   {0} votes for taxes.".format(self.taxes_tally)
            for tweet in self.tax_tweets:
                print "      " + tweet
            print "   {0} votes for whiskey.".format(self.whiskey_tally)
            for tweet in self.whiskey_tweets:
                print "      " + tweet
            if self.sleep(sleepdelay):
                print "Somebody pressed the Big Red Button!"
                self.dunk.dunk_both()
                return 
            countdown -= sleepdelay
        
        print "GAME OVER"
        if self.whiskey_tally == self.taxes_tally:
            print "TIE! Both get dunked!"
            self.dunk.dunk_both()
        if self.whiskey_tally > self.taxes_tally:
            print "WHISKEY WINS!  Taxes gets dunked!"
            self.dunk.dunk_right()
        if self.whiskey_tally < self.taxes_tally:
            print "TAXES WINS!  Whiskey gets dunked!"
            self.dunk.dunk_left()
        print "Taxes:   {0} votes.".format(self.taxes_tally)
        print "Whiskey: {0} votes.".format(self.whiskey_tally)

    def start(self):
        while True:
            if self.confirm(prompt="Next game?"):
                print "Game on!  START START START START START START START START START START START START"
                self.game_loop()
                self.reset_game()

    def sleep(self, delay):
        timeslice = 0.2
        # sleep for half a second, check the button, repeat
        for poll in range(1, delay*int(delay/timeslice)):
            time.sleep(timeslice)
            if self.dunk.check_big_red_button():
                return True
        return False

print "Starting up..."
whiskey_game = WhiskeyGame()
whiskey_game.start()
