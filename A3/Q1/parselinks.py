import sys
import subprocess
from bs4 import *
import urllib2
import re

if len(sys.argv) != 2:
	print "Usage: Python parselinks.py <file_name>"
	print "e.g: Python parselinks.py uniquelinks.txt"
	exit()
def visible(element):
	if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
		return False
	elif re.match(r"[\s\r\n]+",unicode(element)): 
		return False
	return True

fh_input = open(sys.argv[1], 'r')
fh_map = open("map.txt", 'w')
for link in fh_input:
	try:
		cmd = 'echo -n "' + link + '" | md5sum'
		output = subprocess.check_output(cmd, shell=True)
		output_file_name = output[0:32]
		html_page = urllib2.urlopen(link)
		soup = BeautifulSoup(html_page, "html.parser")
		texts = soup.findAll(text=True)
		output_texts = str(texts)
		fh_output = open(output_file_name, 'w')
		fh_output.write(output_texts)
		fh_output.close()
		output_file_name_processed = output_file_name + '.processed'
		fh_output_processed = open(output_file_name_processed, 'w')
		visible_texts = filter(visible, texts)
		output_texts =  str (visible_texts)
		fh_output_processed.write(output_texts)
		fh_output_processed.close()
		fh_map.write(link)
		fh_map.write('\t')
		fh_map.write(output_file_name_processed)
		fh_map.write('\n')
	except:
		print "This link generated an error code:"
		print link
fh_input.close()
fh_map.close()
