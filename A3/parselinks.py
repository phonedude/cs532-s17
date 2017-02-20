import sys
import subprocess
from bs4 import *
import urllib2
import re

if len(sys.argv) != 2:
	print "Usage: Python parselinks.py <file_name>"
	print "e.g: Python parselinks.py uniquelinks.txt"
else:
	fh_input = open(sys.argv[1], 'r')
	for link in fh_input:
    try:
        html_page = urllib2.urlopen(link)
        soup = BeautifulSoup(html_page, "html.parser")
        #hash link here to get output file name
        texts = soup.findAll(text=True)

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

visible_texts = filter(visible, texts)

#########################################################3
        output_file_name = link
            output_file_name = sys.argv[2] + str(i)
            fh_json_output = open(output_file_name, "w")
            json.dump(content, fh_json_output)
            fh_output.write(line)
	    i = i + 1
            fh_json_output.close()
        except:
            print "This link came with an error code:"
            print "http://memgator.cs.odu.edu/timemap/json/" + line
fh_input.close()
