fileName = input("Enter file name: ")
if len(fileName) < 1:
    fileName = "mbox-short.txt"

fileHandle = open(fileName)
listHour = list()
counts = dict()

for line in fileHandle:
    if line.startswith('From '):
        wordsOfLine = line.split()
        time = wordsOfLine[5]
        HourMinuteSecond = time.split(':')
        listHour.append(HourMinuteSecond[0])
        
for hour in listHour:
    counts[hour] = counts.get(hour,0) + 1
    
listTuple = list()
for key,val in counts.items():
    newTuple = (key,val)
    listTuple.append(newTuple)
    
listTuple.sort()

for tup in listTuple:
    print(tup[0],tup[1])