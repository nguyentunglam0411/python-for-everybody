# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:13:52 2023

@author: MPTCDT
"""

#Option 1
handleFile = open('mbox-short.txt')
for line in handleFile:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)
        
#Example get email
print('--------------------')
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        email = re.findall('\S+?@\S+', line)
        print(email)

        #add = re.findall('^From:.*@([^ ]*)', line)
        #print(add)

#Example get number
print('--------------------')
myString= 'My 2.3 favorite number are 22 and 11'
numberOfString = re.findall('[a-z0-9]', myString)
print(numberOfString)
y = re.findall('[AEIOU]+', myString)
print(y)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)