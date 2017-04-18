import sys

if len(sys.argv) < 3:
	print "Usage: python makeunique.py <input_file> <output_file>"
	print "e.g: python makeunique.py links.txt uniquelinks.txt"
else: 
	seen_lines = set()
	outputfile = open(sys.argv[2], "w")
	for line in open(sys.argv[1], "r"):
    		if line not in seen_lines:
        		outputfile.write(line)
        		seen_lines.add(line)
outputfile.close()
