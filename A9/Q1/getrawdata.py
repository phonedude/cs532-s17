import sys
import urllib2

if len(sys.argv) != 2:
	print "Usage: python getrawdata.py <feed_urls_input_file>"
	print "e.g: python getrawdata.py pages.txt"
	exit()
	
fh_input = open (sys.argv[1], 'r')
urls = []

for line in fh_input:
	urls.append(line.rstrip())

counter = 1
for url in urls:
	response = urllib2.urlopen(url)
	page = response.read()
	output_file = str(counter) + '.RawRSS'
	fh_output = open(output_file, 'w')
	fh_output.write(page)
	fh_output.close()
	counter = counter + 1

fh_input.close()
