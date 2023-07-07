# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:30:11 2023

@author: Tung-Lam Nguyen
"""

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    shout = line.rstrip().upper()       # Removes newline and capitalizes
    print(shout)