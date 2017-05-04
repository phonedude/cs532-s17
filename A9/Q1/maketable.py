import sys

if len(sys.argv) != 2:
	print "Usage: python maketable.py <input_file>"
	print "e.g: python maketable.py 100rss.txt"
	exit()
	
fh_input = open (sys.argv[1], 'r')
titles = []

for line in fh_input:
	line = line.split('|')
	title = line[0].strip()
	titles.append(title)

fh_output = open('tex.table','w')
fh_output.write('\\begin{longtable}{ |p{12cm}|p{2cm}| }'+'\n')
fh_output.write('\hline'+'\n')
fh_output.write('Title'+'\n')
fh_output.write('&'+'\n')
fh_output.write('Classification'+' \\\\ '+'\n')

for title in titles:
	fh_output.write('\hline'+'\n')
	fh_output.write(title)
	fh_output.write('\n&\n')
	fh_output.write('class'+' \\\\ '+'\n')

fh_output.write('\end{longtable}')
fh_input.close()
fh_output.close()
