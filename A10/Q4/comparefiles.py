import sys
import os
import re

if len(sys.argv) != 2:
	print "Usage: python comparefiles.py <map_file>"
	print "e.g: python comparefiles.py map.txt"
	exit()

map_file = open(sys.argv[1] ,"r")
raw_output = open("rawdiff.txt" ,"w")
processed_output = open("processeddiff.txt", "w")

raw_file_names = []

counter = 0
for line in map_file:
	if (counter % 2 == 1):
		line = line.strip()
		line = re.sub('\.processed$', '', line)
		raw_file_names.append(line)
 	counter = counter + 1

for name in raw_file_names:
	try:
		rawold = os.path.getsize("rawold/" + name)
		rawnew = os.path.getsize("rawnew/" + name)
		diff = rawold - rawnew
		raw_output.write(str(diff) + "\n")
		processedold = os.path.getsize("processedold/" + name + ".processed")
		processednew = os.path.getsize("processednew/" + name + ".processed")
		diff = processedold - processednew
		processed_output.write(str(diff) + "\n")
	except:
		print 'File does not exist because the URI did not return "200 OK"'

map_file.close()
raw_output.close()
processed_output.close()
