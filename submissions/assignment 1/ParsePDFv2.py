#!/usr/bin/python2.7

import re
import requests
from bs4 import BeautifulSoup
from sys import argv

url = argv[1]

resp = requests.get(url)
soup = BeautifulSoup(resp.content)

print "STARTING URI: " + url

for link in soup.find_all('a',href=True):
	current_link = link.get('href')
	if current_link.endswith('pdf'):
		print("STARTING URI: " + url)
		print("FINAL PDF LINK: " + current_link)
		response = requests.head(current_link)
		size=response.headers['content-length']
		print("FINAL PDF SIZE: " + size)
		print("-----")