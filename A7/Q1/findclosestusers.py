import sys

if len(sys.argv) < 2:
	print "Usage: python findclosestusers.py <input_file>"
	print "e.g: python findclosestusers.py u.user"
	exit()

users = []
fh_output = open('closest3users.txt', 'w')

with open(sys.argv[1]) as fp_input:
	for line in fp_input:
        	users.append(line.split('|'))		
		
for user in users:
	if (user[1] < '37' and user[1] > '34' and user[2] == 'M' and user[3] == 'programmer'):
		fh_output.write(str(user[0])+'|')
		fh_output.write(str(user[1])+'|')
		fh_output.write(str(user[2])+'|')
		fh_output.write(str(user[3])+'|')
		fh_output.write(str(user[4]))
		
fp_input.close()
fh_output.close()
