import sys
import urllib2
import json
if len(sys.argv) != 4:
    print "Usage: Python downloadtimemapsjson.py <input_file> <output_file1> <output_file2>"
    print "e.g: Python downloadtimemapsjson.py uniquelinks.txt timemap.json uniquelinkswithmemes.txt"
else:
    i = 1 
    fh_input = open(sys.argv[1], 'r')
    fh_output = open(sys.argv[3], 'w')
    for line in fh_input:
        try:
            link =  "http://memgator.cs.odu.edu/timemap/json/" + line
            response = urllib2.urlopen(link)
            content = json.load(response)
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
    fh_output.close()
