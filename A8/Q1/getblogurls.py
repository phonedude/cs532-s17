import sys
from bs4 import BeautifulSoup
import urllib2
import re

fh_output = open('urls.txt','w')
fh_output.write('http://f-measure.blogspot.com/'+'\n')
fh_output.write('http://ws-dl.blogspot.com/'+'\n')

for i in range(200):
	try:
		url = 'http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117'
		html_page = urllib2.urlopen(url)
		html = html_page.read()
		soup = BeautifulSoup(html, "html.parser")
		for link in soup.find_all('link'):
			if link['rel']==['alternate'] and link['type']=='application/atom+xml':
				blog_url = link['href']
				blog_url = blog_url[:-19]  	
				fh_output.write(blog_url+'\n')
	except:
		continue
fh_output.close()
