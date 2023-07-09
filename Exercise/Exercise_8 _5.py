# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 18:39:24 2023

@author: Tung-Lam Nguyen
"""

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith('From '):
        wordsOfLine = line.split()
        print(wordsOfLine[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
