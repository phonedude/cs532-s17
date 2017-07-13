import sys
import json
import os
if len(sys.argv) != 3:
	print "Usage: Python parsejsontimemap.py <input_file> <output_file>"
	print "e.g: Python parsejsontimemap.py timemap.json timemapreport.txt"
else:
	fh_output = open(sys.argv[2] , 'w')
	fh_output10 = open('linksnmemesnumA10.txt', 'w')
	for i in range(1,464):
		input_file_name = sys.argv[1] + str(i)
		data_file = open(input_file_name, 'r')
		data = json.load(data_file)
		N = len(data['mementos']['list'])
		fh_output10.write(data['original_uri'] + '\t' + str(N))
		N = str(N)	
		fh_output.write(N)
		fh_output.write("\n")
		fh_output10.write('\n')
		data_file.close()
	fh_output.close()
	fh_output10.close()
	
