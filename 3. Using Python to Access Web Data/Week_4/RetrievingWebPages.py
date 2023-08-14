# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 10:01:01 2023

@author: nguye
"""

import urllib.request, urllib.parse, urllib.error

fileHandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

count = dict()
for line in fileHandle:
    words = line.decode().strip()
    for word in words:
        count[word] = count.get(word,0) + 1
print(count)

print('--------------------------')
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for lineInFile in fhand:
    print(lineInFile.decode().strip())