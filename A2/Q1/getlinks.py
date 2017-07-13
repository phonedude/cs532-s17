#!/usr/bin/env python
import sys
import re
import requests
import urllib2
from urlparse import urlparse
import tweepy
#config.py contains your twitter's API consumer_key, consumer_secret, access_key, and access_secret
config = {}
execfile("config.py", config)
#method to get a user(s) last  200 tweets
def get_tweets(username):
	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
	auth.set_access_token(config["access_key"], config["access_secret"])
	api = tweepy.API(auth)
	#set count to however many tweets you want; twitter only allows 200 at once
	number_of_tweets = 200
	#get tweets
	tweets = api.user_timeline(screen_name = username,count = number_of_tweets)
	final_urls = []
	for tweet in tweets:
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet.text)
		for url in urls:
			#keep external links and throw out links in tweets that lead to other tweets
			try:
				res = urllib2.urlopen(url)
				actual_url = res.geturl()
				parsed_uri = urlparse(actual_url)
				domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
				if (domain != 'https://twitter.com/' and domain != 'https://t.co/'):
					final_urls.append(actual_url)
			except:
				print "Discarded url: The url is not external: " + url
	fh = open ("links.txt", "a")
	#remove duplicates
	final_urls = list(set(final_urls))
	#save links
	for link in final_urls:
		fh.write(link)
		fh.write("\n")
	fh.close()
if __name__ == '__main__':
	if len(sys.argv) >= 2:
		i = 1
		#loop over all users entered as command line arguments and get their tweets (200 total allowed)
		for user in sys.argv:
				if (i < len(sys.argv)):
					get_tweets(sys.argv[i])
					i = i + 1
	else:
		print "Error: You did not enter twitter username(s)"
		print "Usage: Python get_links.py <twitter_username1> <twitter_username2> <twitter_username3> ...etc"
		print "e.g: Python get_links.py phonedude_mln HussamHallak1 weiglemc cnn Aljazeera"
		print "Note 1: Twitter limits this program to 200 tweets per request!"
		print "Note 2: Links not external to Twitter are not saved!"
