import sys
from scipy import spatial

def readfile(filename):
	lines = [line for line in open(filename)]
	colnames = lines[0].strip().split('\t')[1:]
	rownames = []
	data = []
	for line in lines[1:]:
		p = line.strip().split('\t')
		rownames.append(p[0])
		data.append([float(x) for x in p[1:]])
	return (rownames, colnames, data)

def cosine(v1,v2):
	return spatial.distance.cosine(v1,v2)

def getdistances(data,vec1):
	distancelist=[]
	for i in range(len(data)):
		vec2=data[i]
		distancelist.append((cosine(vec1,vec2),i))
	distancelist.sort()
	return distancelist

def knnestimate(blogs, data,vec1,k):
	dlist=getdistances(data,vec1)
	for i in range(k):
		print str(dlist[i][0])
		print str(blogs[dlist[i][1]])
	return dlist

def main():
	if len(sys.argv) < 2:
		print "Usage: python getpages.py <input_file>"
		print "e.g: python getpages.py blogdata.txt"
		exit()

	(blogs,words,data) = readfile(sys.argv[1])
	ks = [1,2,5,10,20]

	counter = 0
	for blog in blogs:
		if (blog == "F-Measure"):
			fm = blog
			blogdata = data[counter]
			blogs.pop(counter)
			data.pop(counter)
			counter = counter + 1
	
	print fm
	print "=============="

	for k in ks:
		print 'For K = ', k, ' :'
		print '******************'
		knnestimate(blogs, data, blogdata, k)
	
	blogs.append(fm)
	data.append(blogdata)

	print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"

	counter = 0
	for blog in blogs:
		if (blog == "Web Science and Digital Libraries Research Group"):
			wsdl = blog
			blogdata = data[counter]
			blogs.pop(counter)
			data.pop(counter)
			counter = counter + 1

	print wsdl
	print "=============="
        for k in ks:
                print 'For K = ', k, ' :'
                print '******************'
                knnestimate(blogs, data, blogdata, k)


if __name__ == "__main__":
    main()
