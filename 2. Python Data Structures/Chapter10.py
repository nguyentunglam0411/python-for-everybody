fileName = input("Enter file name: ")
if len(fileName) < 1:
    fileName = "mbox-short.txt"

fileHandle = open(fileName)
listEmail = list()
counts = dict()

for line in fileHandle:
    if line.startswith('From '):
        wordsOfLine = line.split()
        print(wordsOfLine)