import sys
import docclass
import re
import math

if len(sys.argv) < 4:
	print "Usage: python predict.py <grounnd_truth_file> <train_num> <predict_num>"
	print "e.g: python predict.py actual.txt 90 10"
	exit()
fh_input = open(sys.argv[1],'r')
file_name = 'predictedtable' + sys.argv[2] + '_' + sys.argv[3] + '.txt'
fh_output = open(file_name,'w')

titles = []
cats = []
predictions = []
train_num = int (sys.argv[2])
predicted_num = int (sys.argv[3])
max_data = train_num + predicted_num
count = 0

for line in fh_input:
	item = line.strip()
	item = item.split('|')
	cat = item[1]
	title = item[0]
	cats.append(cat)
	titles.append(title)
  
cl = docclass.fisherclassifier(docclass.getwords)
cl.setdb('hhallak.db')

while count < train_num:
	cl.train(title, cats[count])
	count = count + 1

while count < max_data:
	prediction = cl.classify(titles[count])
	predictions.append(prediction)
	count = count + 1

fh_output.write("Title" + '|' + "Actual" + '|' + "Predicted" + '\n')

for i in range(0,predicted_num):
	fh_output.write(titles[i+train_num] + '|' + cats[i+train_num] + '|' + predictions[i] + '\n')	
fh_input.close()
fh_output.close()
