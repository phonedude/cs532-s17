import sys
import numpy as np
import urllib2
import re

if len(sys.argv) != 2:
	print "Usage: Python parse.py <file_name>"
	print "e.g: Python parse.py mln.graphml"
	exit()

fh_input = open(sys.argv[1], 'r')
fh_output = open("friendscount.txt", 'w')
friends = []
total = 0

for tag in fh_input:
	if 'key="friend_count' in tag:
		num = tag[35:]
		num = num[:-11]
		num = int(num)
		total = total + num
		friends.append(num)

npar = np.array(friends)
median = np.median(npar)
count = float(len(friends))
mean = total/count
print 'Total friends of friends of mln including his:'
print total
print 'mln friends count:'
print len(friends)
print 'Mean:'
print round(mean, 1)
print 'Median:'
print round(median, 1)
print "STD:"
print round(np.std(friends), 1) 

friends.append(len(friends))
friends.sort()
for number in friends:
        number = str(number)
        fh_output.write(number)
        fh_output.write('\n')

fh_input.close()
fh_output.close()
