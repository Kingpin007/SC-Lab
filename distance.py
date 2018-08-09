# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 09:18:34 2018

@author: VP LAB
"""
import numpy
fuzzySet1 = list(tuple())
fuzzySet2 = list(tuple())
l1 = list()
l2 = list()
x = int(input("Enter the number of elements: "))
element = 1;
print("Enter elements for the set1: ")
for i in range(x):
    a = float(input("Enter element for fuzzy set 1:"))
    l1.append(a)
    fuzzySet1.append((element,a))
    element += 1
element = 1
print("Enter elements for the set2: ")
for i in range(x):
    a = float(input("Enter element for fuzzy set 2: "))
    fuzzySet2.append((element,a))
    l1[i] = l1[i] - a
    element += 1
print("FUZZY SET 1: ")
for currentSet in fuzzySet1:
    print(currentSet,end=",")
print("\nFUZZY SET 2: ")
for currentSet in fuzzySet2:
    print(currentSet,end=",")
ed = round((numpy.linalg.norm(numpy.array(l1))),4)
hd = 0
for i in l1:
    hd += round(abs(i),4)
print("\nEuclidean distance : " + str(ed))
print("\nNormalized Euclidean distance : " + str(ed/x))
print("\nHamming distance : " + str(hd))
print("\nNormalized Hamming distance : " + str(hd/x))
