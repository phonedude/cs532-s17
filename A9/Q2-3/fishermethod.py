import re
import math
import feedparser
import requests
from bs4 import BeautifulSoup as bs
from sqlite3 import dbapi2 as sqlite
import os
import pandas_ml as pd

header={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36', 'Accept-Language':'en'}




def F_P_R(articles, classifier):
    categories=classifier.categories()
    values=list((k,v) for k,v in articles.values())
    pred=list(v for k,v in values)
    act=list(k for k,v in values)
    pred=[item.rstrip() for item in pred]
    act=[item.rstrip() for item in act]
    conf=pd.ConfusionMatrix(act,pred)
    conf.print_stats()
   
            
    
                      
    
def downtohundred(path):
    articles={}
    for file in os.listdir(path):
        filepath=os.path.join(path, file)
        d=feedparser.parse(filepath)
        for e in d.entries:
            if 'summary' in e:
                articles.setdefault(e.title, e.summary)
            else:
                articles.setdefault(e.title, e.description)
    return [(v, k) for v,k in articles.items()][:100]

    


# Takes a filename of URL of a blog feed and classifies the entries
def read(feed,classifier):
    # Get feed entries and loop over them
    f=feedparser.parse(feed)
    for entry in f.entries:
        if 'summary' in entry:
            text=entry.summary
        else:
            text=entry.description
        print('\n-----')
        # Print the contents of the entry
        print('Title: '+entry.title.encode('utf-8'))
        print('Published: '+entry.published.encode('utf-8'))
        print('\n'+text.encode('utf-8'))
        # Combine all the text to create one item for the classifier
        fulltext='%s\n%s\n%s' % (entry.title,entry.published,text)
        # Print the best guess at the current category
        print('Guess: '+str(classifier.classify(fulltext)))
        # Ask the user to specify the correct category and train on that
        cl=raw_input('Enter category: ')
        classifier.train(fulltext,cl)


#my take on the read function. takes a list of titles to be found in a file of feeds       
def myread(articles, path, classifier):
    entries=[]
    for file in os.listdir(path):
        feed=os.path.join(path, file)
        f=feedparser.parse(feed)
        for entry in f.entries:
            entries.append(entry)
    
    for entry in entries:
        if entry.title in articles.keys():
            if 'summary' in entry:
                text=entry.summary
            else:
                text=entry.description
            print('\n-----')
            # Print the contents of the entry
            print('Title: '+ str(entry.title))
            print('\n'+str(text))
            # Combine all the text to create one item for the classifier
            fulltext='%s\n%s' % (entry.title,text)
            # Print the best guess at the current category
            print('Guess: '+str(classifier.classify(fulltext)))
            # Ask the user to specify the correct category and train on that
            cl=input('Enter category: ')
            classifier.train(fulltext,cl)

            
def myclassify(articles, path, classifier):
    entries=[]
    for file in os.listdir(path):
        feed=os.path.join(path, file)
        f=feedparser.parse(feed)
        for entry in f.entries:
            entries.append(entry)

    for entry in entries:
        if entry.title in articles.keys():
            if 'summary' in entry:
                text=entry.summary
            else:
                text=entry.description
            fulltext='%s\n%s' % (entry.title,text)
            best=classifier.classify(fulltext)
            articles[entry.title]=(articles[entry.title], best)
            
    if not os.path.exists('./results'):
        os.mkdirs('./results')
    file=os.path.join('./results/','results'.rstrip()+str(len(os.listdir('./results')))+'.txt')
    with open(file, 'w') as out:
        for key in articles.keys():
            print(key, *articles[key], sep='\t', end='\n', file=out)
    F_P_R(articles, classifier)
    
        


def getwords(doc):
    splitter=re.compile('\\W*')
    # Split the words by non-alpha characters
    words=[s.lower( ) for s in splitter.split(doc)
if len(s)>2 and len(s)<20]
    # Return the unique set of words only
    return dict([(w,1) for w in words])


class classifier:
    def __init__(self,getfeatures,filename=None):
        # Counts of feature/category combinations
        self.fc={}
        # Counts of documents in each category
        self.cc={}
        self.getfeatures=getfeatures

    # Increase the count of a feature/category pair
    def incf(self,f,cat):
        count=self.fcount(f,cat)
        if count==0:
            self.con.execute("insert into fc values ('%s','%s',1)"% (f,cat))
        else:
            self.con.execute("update fc set count=%d where feature='%s' and category='%s'"% (count+1,f,cat))

    # Increase the count of a category
    def incc(self,cat):
        count=self.catcount(cat)
        if count==0:
            self.con.execute("insert into cc values ('%s',1)" % (cat))
        else:
            self.con.execute("update cc set count=%d where category='%s'" % (count+1,cat))

    # The number of times a feature has appeared in a category
    def fcount(self,f,cat):
        res=self.con.execute('select count from fc where feature="%s" and category="%s"'%(f,cat)).fetchone( )
        if res==None:
            return 0
        else: return float(res[0])

    # The number of items in a category
    def catcount(self,cat):
        res=self.con.execute('select count from cc where category="%s"'%(cat)).fetchone( )
        if res==None:
            return 0
        else:
            return float(res[0])

    # The total number of items
    def totalcount(self):
        res=self.con.execute('select sum(count) from cc').fetchone( )
        if res==None:
            return 0
        return res[0]

    # The list of all categories
    def categories(self):
        cur=self.con.execute('select category from cc')
        return [d[0] for d in cur]

    def train(self,item,cat):
        features=self.getfeatures(item)
        # Increment the count for every feature with this category
        for f in features:
            self.incf(f,cat)
        # Increment the count for this category
        self.incc(cat)
        self.con.commit( )

    def fprob(self,f,cat):
        if self.catcount(cat)==0:
            return 0
        # The total number of times this feature appeared in this
        # category divided by the total number of items in this category
        return self.fcount(f,cat)/self.catcount(cat)

    def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
        # Calculate current probability
        basicprob=prf(f,cat)
        # Count the number of times this feature has appeared in
        # all categories
        totals=sum([self.fcount(f,c) for c in self.categories( )])
        # Calculate the weighted average
        bp=((weight*ap)+(totals*basicprob))/(weight+totals)
        return bp

    def setdb(self,dbfile):
        self.con=sqlite.connect(dbfile)
        self.con.execute('create table if not exists fc(feature,category,count)')
        self.con.execute('create table if not exists cc(category,count)')




    

class fisherclassifier(classifier):
    def __init__(self,getfeatures):
        classifier.__init__(self,getfeatures)
        self.minimums={}
    
    def cprob(self,f,cat):
        # The frequency of this feature in this category
        clf=self.fprob(f,cat)
        if clf==0:
            return 0
        # The frequency of this feature in all the categories
        freqsum=sum([self.fprob(f,c) for c in self.categories( )])
        # The probability is the frequency in this category divided by
        # the overall frequency
        p=clf/(freqsum)
        return p

    def fisherprob(self,item,cat):
        # Multiply all the probabilities together
        p=1
        features=self.getfeatures(item)
        for f in features:
            p*=(self.weightedprob(f,cat,self.cprob))
            # Take the natural log and multiply by -2
            fscore=-2*math.log(p)
        # Use the inverse chi2 function to get a probability
        return self.invchi2(fscore,len(features)*2)

    def invchi2(self,chi,df):
        m = chi / 2.0
        sum = term = math.exp(-m)
        for i in range(1, df//2):
            term *= m / i
            sum += term
        return min(sum, 1.0)

    def setminimum(self,cat,min):
        self.minimums[cat]=min

    def getminimum(self,cat):
        if cat not in self.minimums:
            return 0
        return self.minimums[cat]

    def classify(self,item,default=None):
        # Loop through looking for the best result
        best=default
        max=0.0
        for c in self.categories( ):
            p=self.fisherprob(item,c)
            # Make sure it exceeds its minimum
            if p>self.getminimum(c) and p>max:
                best=c
                max=p
        return best

    

    
