#! /usr/bin/python
import sys
import feedparser
import socket
if len(sys.argv) < 2:
	print "Usage: python downloadrss.py <feed_url>"
	print "e.g: python downloadrss.py http://tutorialsprogram.blogspot.com/feeds/posts/default"
	exit()
timeout = 120
socket.setdefaulttimeout(timeout)
feed_url = sys.argv[1]
d = feedparser.parse(feed_url)
fh_output = open('rss.txt', 'a')
for s in d.entries:
	fh_output.write(unicode(s.title).encode("utf-8") + "|" + unicode(s.link).encode("utf-8") + "\n")
