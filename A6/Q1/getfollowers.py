import sys
import time
import tweepy

if len(sys.argv) < 2:
	print "Usage: Python getfollowers.py <twitter_userid>"
	print "e.g: Python getfollowers.py phonedude_mln"
	exit()
username = sys.argv[1]
#config.py contains your twitter's API consumer_key, consumer_secret, access_key, and access_secret
config = {}
execfile("config.py", config)
auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
auth.set_access_token(config["access_key"], config["access_secret"])
api = tweepy.API(auth)

users = tweepy.Cursor(api.followers, screen_name=username).items()

filename = username + 'FOLLOWERS.txt'
fh_output = open(filename, "w")
fh_output.write(username + '\n')

while (1):
    try:
        user = next(users)
	fh_output.write(user.screen_name + '\n')
    except tweepy.TweepError:
        time.sleep(60)
fh_output.close()
