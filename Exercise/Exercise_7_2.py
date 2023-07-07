# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:32:29 2023

@author: Tung-Lam Nguyen
"""

#Variables
count = 0
total = 0

# Use mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ',fname)
    quit()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        position = line.find(':')
        stringNumber = line[position+1:].strip()
        number = float(stringNumber)
        
        total = total + number

average = total/count
print('Average spam confidence:', average)