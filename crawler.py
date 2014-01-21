#!/usr/bin/env python 
import urllib2
from BeautifulSoup import BeautifulSoup
from optparse import OptionParser

__author__='Saurav'

###Basic implementation of a webcrawler that takes a seed url and crawls all
###links that are reachable by it 

def isValidUrl(url):
    '''Returns True or False depending on a regex matching'''
    #TODO: Improve using regex matching 
    pass 

def crawler(seedUrl):
     toCrawl=[seedUrl] 
     crawled=[]
     print "Starting the Crawler..."
     while len(toCrawl) != 0:
       urlToCrawl=toCrawl.pop() 
       print "Crawling page : " , urlToCrawl
       try:
         html=urllib2.urlopen(urlToCrawl)
       except urllib2.HTTPError as e:
          print e.code
       except urllib2.URLError as e:
          print e.reason
       else: 
          pagesource=html.read()
          soup=BeautifulSoup(pagesource)
          linksInPage=soup.findAll('a',href=True) 
          listlinks=[] 
          for l in linksInPage:
           if l['href'][:4]=='http':
             listlinks.append(l['href'])
          linksInPage=listlinks
          if urlToCrawl not in crawled:
            #avoid cycles 
            for link in linksInPage:
                   toCrawl.append(link)
            crawled.append(urlToCrawl)
     assert len(toCrawl) == 0
     return crawled 


if __name__=="__main__":
    parser=OptionParser() 
    parser.add_option("-u","--url",dest="seed",help="supply a starting url to start crawling")
    options,args=parser.parse_args() 
    seed=options.seed
    crawled_links=crawler(seed)
    print "Number of pages crawled : "  , len(crawled_links)
