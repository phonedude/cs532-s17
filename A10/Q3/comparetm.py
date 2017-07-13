import sys 

if len(sys.argv) != 3:
	print "Usage: python comparetm.py <input_file_1> <input_file_2>"
	print "e.g: python comparetm.py linksnmemesnumA2.txt linksnmemesnumA10.txt"
	exit()
A2 = open(sys.argv[1], 'r')
A10 = open(sys.argv[2], 'r')
output = open('graphtm.txt', 'w')

list2 = []
list10 = []
outlist = []

for line in A2:
	temp = []
	line = (line.strip()).split('\t')
	temp.append(line[0])
	temp.append(line[1])
	list2.append(temp)

for line in A10:
	temp = []
	line = (line.strip()).split('\t')
        temp.append(line[0])
        temp.append(line[1])
        list10.append(temp)

for key2,value2 in list2:
	for key10,value10 in list10:
		if (key2 == key10):
			diff = int(value2) - int(value10)
			outlist.append(diff)

for item in outlist:
	output.write(str(item))
	output.write('\n')	

A2.close()
A10.close()
output.close()

