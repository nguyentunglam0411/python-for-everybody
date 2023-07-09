# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 18:39:24 2023

@author: Tung-Lam Nguyen
"""

fileName = input("Enter file name: ")
if len(fileName) < 1:
    fileName = "mbox-short.txt"

fileHandle = open(fileName)
listEmail = list()
counts = dict()

for line in fileHandle:
    if line.startswith('From '):
        wordsOfLine = line.split()
        listEmail.append(wordsOfLine[1])
        
for email in listEmail:
    counts[email] = counts.get(email,0) + 1
    
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        
print(bigword,bigcount)