import sys
import feedparser
import re

if len(sys.argv) < 2:
        print "Usage: python generatefeedvector.py <input_file>"
        print "e.g: python generatefeedvector.py pages.txt"
        exit()

def getwordcounts(url):
    d=feedparser.parse(url)
    wc={}

    for e in d.entries:
        if 'summary' in e:
		summary=e.summary
        else:
		summary=e.description
        
        words=getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word,0)
            wc[word]+=1
    return d.feed.title,wc

def getwords(html):
    txt=re.compile(r'<[^>]+>').sub('',html)
    words=re.compile(r'[^A-Z^a-z]+').split(txt)
    return [word.lower( ) for word in words if word!='']

apcount={}
wordcounts={}
feedlist=[line for line in open(sys.argv[1],'r')]
for feedurl in feedlist:
    try:
	title,wc=getwordcounts(feedurl)
	wordcounts[title]=wc
	for word,count in wc.items( ):
		apcount.setdefault(word,0)
		if count > 1:
			apcount[word]+=1
    except:
	print "Error in parsing: "
	print feedurl

wordlist2 = []
for w,bc in apcount.items( ):
    frac=float(bc)/len(feedlist)
    if frac > 0.1 and frac < 0.5: 
	wordlist2.append([bc,w])

wordlist2.sort(key=lambda tup:tup[1], reverse=True)

out=open('blogdata.txt','w')
out.write('Blog')
for i in range(min(len(wordlist2),1000)): 
	out.write('\t%s' % wordlist2[i][1])
out.write('\n')
for blog,wc in wordcounts.items( ):
    out.write(blog)
    for i in range(min(len(wordlist2),1000)):
        if wordlist2[i][1] in wc: out.write('\t%d' % wc[wordlist2[i][1]])
        else: out.write('\t0')
    out.write('\n')
out.close()
