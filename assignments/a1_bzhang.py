import urllib.request
from bs4 import BeautifulSoup

uri=input('Please enter a URI\n')
with urllib.request.urlopen(uri) as res:
    html = res.read()
soup = BeautifulSoup(html, "html.parser")

for links in soup.find_all('a'):
    response = urllib.request.urlopen(links.get('href'))
    if response.info()['Content-Type']=='application/pdf':
        print (response.geturl())
        print (response.info()['Content-Length'])
