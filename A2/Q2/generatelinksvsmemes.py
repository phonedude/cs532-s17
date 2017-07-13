import sys
from collections import Counter

if len(sys.argv) != 3:
    print "Usage: python generatelinksvsmemes.py <input_file> <output_file>"
    print "e.g: python generatelinksvsmemes.py timemapreport.txt memesvslinks.txt"
else:
    fh_output = open(sys.argv[2] , 'w')
    number_of_memes = []
    fh_input = open(sys.argv[1], "r")
    
    for line in fh_input:
	line = line.strip('\n')
        number_of_memes.append(line)
    
    fh_output.write('memesCountX')	
    fh_output.write('\t')
    fh_output.write('linksCountY')
    fh_output.write('\n')
    C = Counter(number_of_memes)
    for k,v in C.items():
        fh_output.write(str(k))
	fh_output.write('\t')
	fh_output.write(str(v))
	fh_output.write('\n')
    fh_input.close()
    fh_output.close() 
