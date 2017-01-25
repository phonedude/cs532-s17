import sys
from bs4 import *
import urllib2
import re

if len(sys.argv) != 2:
	print "Usage: Python extracrPDF.py <url>"
	print "e.g: Python extracrPDF.py http://example.com/page.html"
else:
	url = sys.argv[1]
	print "Entered URL:"
	print url
	html_page = urllib2.urlopen(url)
	print "Final URL:"
	print html_page.geturl()
	print "*******************"
	soup = BeautifulSoup(html_page, "html.parser")
	links = []
	for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
		links.append(link.get('href'))
	for link in links:
		try:
			r = urllib2.urlopen(link)
			if r.headers['content-type'] == "application/pdf" and r.getcode() == 200:
				print "Extracted link:"
				print link
				print "Extracted link final URL:"
				print r.geturl()
				print "Size: " + r.headers['Content-Length']
				print "-------------------------------------"
		except urllib2.HTTPError as e:
			print "There is an error extracting PDF files in this link:"
			print "Error Code:"
			print e.code