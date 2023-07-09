# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 18:25:00 2023

@author: Tung-Lam Nguyen
"""
fname = input("Enter file name: ")
fhand = open(fname)

my_list = []

for line in fhand:
    words = line.split()                # Splits line into array of words
    for word in words:
        if word in my_list:
            continue                    # Discards duplicates
        my_list.append(word)            # Updates the list
print(sorted(my_list))                  # Alphabetical order