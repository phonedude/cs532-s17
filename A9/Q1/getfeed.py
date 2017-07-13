import sys
from bs4 import BeautifulSoup
import urllib2
import re
if len(sys.argv) < 2:
	print "Usage: python getfeed.py <feed_url>"
	print "e.g: python getfeed.py http://tutorialsprogram.blogspot.com/feeds/posts/default"
	exit()
fh_output = open('pages.txt', 'w')

def getNextPage(link):
	try:
		html = urllib2.urlopen(link).read()
		soup = BeautifulSoup(html, 'lxml')
		next_page = soup.find('link', rel="next")
		if(next_page != []):
			next_page = next_page.get('href')
			return next_page
	except:
		return False

def getAllPages(link):
	all_pages = []
	next_page = getNextPage(link)
	while(next_page != False):	
		all_pages.append(next_page)
		next_page = getNextPage(next_page)
	return all_pages
   
try:
	html = urllib2.urlopen(sys.argv[1]).read()
	soup = BeautifulSoup(html, 'lxml')
	title = soup.title.string.encode('ascii')
	rss = soup.find('link', type='application/atom+xml')
	rss = rss.get('href')
	pages = getAllPages(rss)
	pages.insert(0,rss)
	for page in pages:
		fh_output.write(page + '\n')
except:
	print 'Error'
fh_output.close()
