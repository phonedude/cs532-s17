import sys
import subprocess
import re

fh_input = open('uniquelinks.txt', 'r')
fh_map = open("map.txt", 'w')
for link in fh_input:
	try:
		cmd = 'echo -n "' + link + '" | md5sum'
		output = subprocess.check_output(cmd, shell=True)
		output_file_name = output[0:32]
		output_file_name_processed = output_file_name + '.processed'
		fh_map.write(link)
		fh_map.write('\t')
		fh_map.write(output_file_name_processed)
		fh_map.write('\n')
	except:
		print "This link generated an error code:"
		print link
fh_input.close()
fh_map.close()
