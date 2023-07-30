# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:49:24 2023

@author: Tung-Lam Nguyen
"""

friends = ['Joseph','Glenn','Sally']
for friend in friends:
    print('Hello ', friend)
print('Done')

#ID of lists start at 0
print(friends[0])
print(friends[1])
print(friends[2])

#Change value in list
print('-----------------------')
friends[0] = 'Simon'
print(friends[0])

print('Length of list: ',len(friends))

#Traversing a list
print("---Traversing a list---")
for i in range(len(friends)):
    print(friends[i])
    
#Building a list
print('-----------------------')
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print('--------------')
print(stuff)

#Check in
print(99 in stuff)
print('Lam' in stuff)
print(100 not in stuff)

#Sort a list
print('-----------------------')
friends.sort()
print(friends)

#Lists and functions
print('-----------------------')
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

#Input
# print('-----------------------')
# total = 0
# count = 0
# while True:
#     inputValue = input('Enter a number: ')
#     if inputValue == 'done': break
#     number = float(inputValue)
#     total = total + number
#     count = count + 1
    
# average = total / count
# print('Average: ',average)

#Lists and Strings
print('-----------------------')
stringValue = 'With three words'
stuff = stringValue.split()
print(stuff)
for word in stuff:
    print(word)
    
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])