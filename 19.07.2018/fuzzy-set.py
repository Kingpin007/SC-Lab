# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

fuzzySet1 = list(tuple())
fuzzySet2 = list(tuple())
inputFile1 = "input-fuzzy-set-1.txt"
inputFile2 = "input-fuzzy-set-2.txt"
file = open(inputFile1,"r")
# Take input from file 1 to get 1st fuzzy set
for line in file:
    lineList = line.split(",");
    lineTuple = (lineList[0],float(lineList[1]))
    fuzzySet1.append(lineTuple)
file.close()
# Take input from file 2 to get 2nd fuzzy set
file = open(inputFile2,"r")
for line in file:
    lineList = line.split(",");
    lineTuple = (lineList[0],float(lineList[1]))
    fuzzySet2.append(lineTuple)
file.close()
# Display Fuzzy Sets
print("FUZZY SET 1: ")
for currentSet in fuzzySet1:
    print(currentSet,end=",")
print("\nFUZZY SET 2: ")
for currentSet in fuzzySet2:
    print(currentSet,end=",")
# UNION operation
print("\nUNION")
unionSet = list(tuple())
for t1 in fuzzySet1:
    for t2 in fuzzySet2:
        if t1[0] == t2[0]:
            newTuple = (t1[0],max(t1[1],t2[1]))
            unionSet.append(newTuple)
            break
for currentSet in unionSet:
    print(currentSet,end=",")
intersectionSet = list(tuple())
print("\nINTERSECTION")
for t1 in fuzzySet1:
    for t2 in fuzzySet2:
        if t1[0] == t2[0]:
            newTuple = (t1[0],min(t1[1],t2[1]))
            intersectionSet.append(newTuple)
            break
for currentSet in intersectionSet:
    print(currentSet,end=",")
differenceSet1 = list(tuple()) 
print("\nSET 1 - SET 2")
for t1 in fuzzySet1:
    for t2 in fuzzySet2:
        if t1[0] == t2[0]:
            newTuple = (t1[0],min(t1[1],1.0-t2[1]))
            differenceSet1.append(newTuple)
            break
for currentSet in differenceSet1:
    print(currentSet,end=",")
differenceSet2 = list(tuple()) 
print("\nSET 2 - SET 1")
for t1 in fuzzySet1:
    for t2 in fuzzySet2:
        if t1[0] == t2[0]:
            newTuple = (t1[0],min(t2[1],round(1.0-t1[1],2)))
            differenceSet2.append(newTuple)
            break
for currentSet in differenceSet2:
    print(currentSet,end=",")
