import sys
import tweepy
from tweepy import *
import time
import numpy as np
if len(sys.argv) < 2:
	print "Usage: python getfollowersdata.py <twitter_username>"
	print "e.g: python getfollowersdata.py phonedude_mln"
	exit()

username = sys.argv[1]
#config.py contains your twitter's API consumer_key, consumer_secret, access_key, and access_secret
config = {}
execfile("config.py", config)
fh_output = open("followerscount.txt", 'w')

if __name__ == '__main__':
	auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
	auth.set_access_token(config["access_key"], config["access_secret"])
	api = tweepy.API(auth)
	data = api.get_user(username)
	followers = []
	total = 0
	for user in tweepy.Cursor(api.followers, screen_name=username, count = 200).items():
		num = int(user.followers_count)
		total = total + num
		followers.append(num)

	npar = np.array(followers)
	median = np.median(npar)
	count = float(len(followers))
	mean = total/count
	print 'Total followers of followers of ', username, ' including his:'
	print total
	print username, '\'s followerss count:'
	print len(followers)
	print 'Mean:'
	print round(mean, 1)
	print 'Median:'
	print round(median, 1)
	print "STD:"
	print round(np.std(followers), 1)
	followers.append(len(followers))
	followers.sort()
	for number in followers:
		if number > 0:
        		number = str(number)
        		fh_output.write(number)
        		fh_output.write('\n')

fh_output.close()

