#!/usr/bin/env python

"""
Download all the pdfs linked on a given webpage

Usage -

    python grab_pdfs.py url <path/to/directory>
        url is required
        path is optional. Path needs to be absolute
        will save in the current directory if no path is given
        will save in the current directory if given path does not exist

Requires - requests >= 1.0.4
           beautifulsoup >= 4.0.0

Download and install using
    
    pip install requests
    pip install beautifulsoup4
"""

__author__= 'elssar <elssar@altrawcode.com>'
__license__= 'MIT'
__version__= '1.0.0'

from requests import get
from urlparse import urljoin
from os import path, getcwd
from bs4 import BeautifulSoup as soup
from sys import argv

def get_page(base_url):
    req= get(base_url)
    if req.status_code==200:
        return req.text
    raise Exception('Error {0}'.format(req.status_code))

def get_all_links(html):
    bs= soup(html)
    links= bs.findAll('a')
    return links

def get_pdf(base_url, base_dir):
    html= get_page()
    links= get_all_links(html)
    if len(links)==0:
        raise Exception('No links found on the webpage')

    for link in links:
        if link['href'][-4:]=='.pdf':

            content= get(urljoin(base_url, link['href']))


            if content.status==200 and content.headers['content-type']=='application/pdf':
                size=req.headers["content-length"]
                print "size"

    if n_pdfs==0:
        raise Exception('No pdfs found on the page')