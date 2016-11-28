#! /usr/bin/env python

from bs4 import BeautifulSoup
from lxml import html
import urllib2,re

#import codecs
#import sys
#streamWriter = codecs.lookup('utf-8')[-1]
#sys.stdout = streamWriter(sys.stdout)

BASE_URL = "http://outlet.us.dell.com/ARBOnlineSales/Online/InventorySearch.aspx?c=us&cs=22&l=en&s=dfh&brandid=2201&fid=111162"

webpage = urllib2.urlopen(BASE_URL)
soup = BeautifulSoup(webpage.read(), "lxml")
findcolumn = soup.find("div", {"id": "itemheader-FN"})
name = findcolumn.text.strip()
print name

#print re.findall("XPS", name)
#print re.findall("5378", name)
#print filter(lambda x: 'XPS' in x, findcolumn)
#print type(findcolumn)#.text
#result = findcolumn.text
#print re.findall(r'XPS', name)
#fo = open("foo.txt", "wb")
#fo.write(findcolumn);
#fo.close()
##print result
