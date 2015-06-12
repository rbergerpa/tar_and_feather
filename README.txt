The public user interface consists of 5 scripts:

setpath.sh - run this first; adds current working directory to the path
run.sh     - runs the game, takes 20-30 second to set up, then prompts y/n to run
both.sh    - dunks both contestants (must control-c to kill game loop)
left.sh    - dunks left contestant  (must control-c to kill game loop)
right.sh   - dunks right contestant (must control-c to kill game loop)

NORMAL OPERATION:

0) $ ./setpath<enter>  this will add current working directory to the path
1) run.sh to start the game
2) initial startup takes 20-30 seconds BEFORE you see any output
3) game will display prompt:  Next game? [n]|y: 
4) press "y" to to start game.
5) after game ends, prompt:  Next game? [n]|y: 
6) press control-c to break out of prompt loop and exit script.

GAME RULES:

120 seconds game duration
 10 second polling loop

Whoever gets the LEAST votes gets "dunked" (spraye with water and feathers).

Vote by tweeting:

@hackpgh @wiglewhiskey #taxes  
@hackpgh @wiglewhiskey #whiskey

Note:  @wiglewhiskey is not a hard requirement

Currently the hashtag can be #tax or #taxes, #whiskey or #whisky

If both hashtags are present, the tweet counts as a vote for both.

Note that there is a 5-10 second delay between tweeting and tweet
showing up in API.

TAXES   == RIGHT WATER and RIGHT FEATHER
WHISKEY == LEFT WATER and LEFT FEATHER

PREEMPTIVE DUNKING

$ right.sh               fires the horn and right feathers & water
$ left.sh                fires the horn and left feathers & water
$ both.sh                fires the horn and both feathers & water

(Note, intent is for whiskey to be left, taxes right)

GOTCHA:  If you preemptively run dunk_right/left/both before the game ends,
         you must control-c to kill the running game.
	 This will also mean

Demo session (30 second game)

----------------------------------------------------------------------
Starting tar and feather game, initial load may take 20-30 seconds.
Starting up...
Next game? [n]|y: y
Game on!  START START START START START START START START START START START START
Polling, 30 seconds left...
   0 votes for taxes.
   0 votes for whiskey.
Polling, 24 seconds left...
   0 votes for taxes.
   0 votes for whiskey.
Polling, 18 seconds left...
   0 votes for taxes.
   0 votes for whiskey.
Polling, 12 seconds left...
   0 votes for taxes.
   0 votes for whiskey.
Polling, 6 seconds left...
   0 votes for taxes.
   0 votes for whiskey.
GAME OVER
TIE! Both get dunked!
Taxes:   0 votes.
Whiskey: 0 votes.
Next game? [n]|y: y
----------------------------------------------------------------------
