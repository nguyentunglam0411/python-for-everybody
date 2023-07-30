# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 09:06:38 2023

@author: Tung-Lam Nguyen
"""

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse['candy'])

#Counting with Dictionaries
# print('----------------------------------')
# counts = dict()
# names = ['csev', 'cwen','csev','zqian', 'cwen']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
        
# print(counts)

#Simplified Counting with get()
# print('----------------------------------')
# counts = dict()
# names = ['csev', 'cwen','csev','zqian', 'cwen']

# for name in names:
#     counts[name] = counts.get(name,0) + 1
# print(counts)

#Counting Pattern
# print('----------------------------------')
# counts = dict()
# print('Enter a line of text: ')
# line = input('')

# words = line.split()
# print('Words: ',words)

# print('Counting...')
# for word in words:
#     counts[word] = counts.get(word,0) + 1
# print('Counts: ',counts)

# for key in counts:
#     print(key, counts[key])
    
# for value1, value2 in counts.items():
#     print(value1,' - ',value2)

#Counting in File
print('----------------------------------')
fileName = input('Enter file: ')
fileHandle = open(fileName)

counts = dict()
for line in fileHandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
        
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        
for y in counts:
    print(y)
        
print(bigword,bigcount)

stuff = dict()
print(stuff.get('candy',-1))