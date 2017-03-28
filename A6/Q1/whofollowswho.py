import sys
import time
from twitter import *
import twitter

if len(sys.argv) < 2:
	print "Usage: python whofollowswho.py <file_name>"
	print "e.g: python whofollowswho.py phonedude_mlnFOLLOWERS.txt"
	exit()

filename = sys.argv[1]
fh_input = open(filename, 'r')
links_output = open("links.csv", 'w')
links_output.write('source,target,type\n')
nodes_output = open("nodes.csv", 'w')
nodes_output.write('node,group\n')
users = fh_input.readlines()
#config.py contains your twitter's API consumer_key, consumer_secret, access_key, and access_secret
config = {}
execfile("config.py", config)
api = twitter.Api(consumer_key=config["consumer_key"], consumer_secret=config["consumer_secret"], access_token_key=config["access_key"], access_token_secret=config["access_secret"], sleep_on_rate_limit=True)
for user in users:
	user = user.strip()
	nodes_output.write(str(user) + ',group1\n')
for user_A in users:
	user_A = user_A.strip()
	for user_B in users:
		user_B = user_B.strip()
		try:
                	result = api.ShowFriendship(source_screen_name = user_A ,target_screen_name = user_B)
                	following = result["relationship"]["target"]["following"]
                	if following:
				links_output.write(user_A + ',' + user_B + ',type1\n')
            	except Exception as err:
                	print(err)
fh_input.close()
links_output.close()
nodes_output.close()
