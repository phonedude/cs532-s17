import sys
from bs4 import BeautifulSoup
import urllib2
import re
if len(sys.argv) < 2:
	print "Usage: python getpages.py <input_file>"
	print "e.g: python getpages.py 100blogs.txt"
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
   
for blog in open(sys.argv[1], 'r'):
	pages = []
	try:
        	html = urllib2.urlopen(blog).read()
        	soup = BeautifulSoup(html, 'lxml')
		title = soup.title.string.encode('ascii')
		rss = soup.find('link', type='application/atom+xml')
		rss = rss.get('href')
		pages = getAllPages(rss)
		pages.insert(0,rss)
		for page in pages:
			fh_output.write(page + '\n')
	except:
		continue
fh_output.close()
