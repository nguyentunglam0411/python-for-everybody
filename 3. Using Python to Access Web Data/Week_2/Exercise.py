# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:08:27 2023

@author: MPTCDT
"""
import re

numlist = list()

handleFile = open('regex_sum_1244581.txt')
for line in handleFile:
    line = line.rstrip()
    stringNum = re.findall('[0-9]+', line)
    if len(stringNum) == 0: continue

    for string in stringNum:
        num = float(string)
        numlist.append(num)

sumOfNumber = sum(numlist)
print('Sum: ', sumOfNumber)