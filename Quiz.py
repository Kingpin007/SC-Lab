# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 09:18:50 2018

@author: Anirudh
"""
import numpy as np

# Max-Product Composition given by Rosenfeld
def maxProduct(x, y):
    z = []
    for x1 in x:
        for y1 in y.T:
            z.append(max(np.multiply(x1, y1)))
    return np.array(z).reshape((x.shape[0], y.shape[1]))

def maxMin(x, y):
    z = []
    for x1 in x:
        for y1 in y.T:
            z.append(max(np.minimum(x1, y1)))
    return np.array(z).reshape((x.shape[0], y.shape[1]))

def cartprod(x, y):
    # Ensure rank-1 input
    x, y = np.asarray(x).ravel(), np.asarray(y).ravel()

    m, n = len(x), len(y)

    a = np.dot(np.atleast_2d(x).T, np.ones((1, n)))
    b = np.dot(np.ones((m, 1)), np.atleast_2d(y))

    return np.fmin(a, b)

def inner_product(a, b):
    return np.max(np.fmin(np.r_[a], np.r_[b]))

def outer_product(a, b):
    return np.min(np.fmax(np.r_[a], np.r_[b]))

def main():
    # 2 arrays for the example
    menu()
    
def menu():
    print("\n\nWelcome to the fuzzy relational operations program you can do the following: ")
    print("1. Max-Min relation")
    print("2. Max-Product relaiton")
    print("3. Complement" )
    print("4. Containment")
    print("5. Exit")
    print("Enter your choice(1-5): ")
    x = int(input())
    if x == 5:
        return
    tempx = x
    x1 = input("Enter dimensions of relations: ").split()
    n, m = int(x1[0]), int(x1[1])
    r1 = list(list())
    r2 = list(list())
    l1 = list()
    print("Enter relation 1: ")
    for i in range(n):
        x = list()
        for j in range(m):
            a = float(input())
            x.append(a)
            l1.append(a)
        r1.append(x)
    print("Enter relation 2: ")
    for i in range(n):
        x = list()
        for j in range(m):
            a = float(input())
            x.append(a)
            l1[i] = l1[i] - a
        r2.append(x)
    r1 = np.array(r1)
    r2 = np.array(r2)
    print("Input relations:\nR1")
    print(r1)
    print("R2")
    print(r2)
    print("R1oR2 ==> Inner Product: " + str(inner_product(r1,r2)))
    print("R1oR2 ==> Outer Product: " + str(outer_product(r1,r2)))
    ed = round((np.linalg.norm(np.array(l1))),4)
    hd = 0
    for i in l1:
        hd += round(abs(i),4)
    print("\nEuclidean distance : " + str(ed))
    print("\nHamming distance : " + str(hd))
    r3 = list(list())
    x = tempx
    if x == 1: 
        print("R1oR2 => Max-Min :\n" + str(maxMin(r1, r2)) + "\n")
    elif x == 2:
        print("R1oR2 => Max-Product :\n" + str(maxProduct(r1, r2)) + "\n\n")
    elif x == 3:
        for i in range(n):
            for j in range(m):
                r1[i][j] = 1 - r1[i][j]
        print("R1 => Complement: \n: " + str(r1))
    elif x == 4:
        for i in range(n):
            x = list()
            for j in range(m):
                if r1[i][j] <= r2[i][j]:
                    x.append(1)
                else:
                    x.append(0)
            r3.append(x)
        r3 = np.array(r3)
        print("R1oR2 => Containment :\n " + str(r3))
    menu()
    
if __name__ == '__main__':
    main()
