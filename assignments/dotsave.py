import urllib2
import re

def getlinks(website):
    openWebsite = urllib2.urlopen(website)
    domain=re.findall('((http|ftp).+[.].?..[/])',website)
    domainName=domain[0][0]
    domainName=domainName[:-1]
    html=openWebsite.read()
    allPdflinks=re.findall('="[^"]+[.]pdf"',html)
    alllinks=re.findall('"((http|ftp)s?://.*?)"',html)
    i=0
    i2=0
    i2=len(allPdflinks)
    while (i<i2):
        allPdflinks[i]=allPdflinks[i][2:]
        allPdflinks[i]=allPdflinks[i][:-1]
        if(not(allPdflinks[i].startswith('http') or allPdflinks[i].startswith('ftp'))):
            allPdflinks[i]=domainName+allPdflinks[i]
        i+=1
    i=0
    while (i<i2):
        try:
            print allPdflinks[i]+" is "+urllib2.urlopen(allPdflinks[i]).headers["content-length"]+" bytes"
        except:
            i=i+0
        i+=1
   
