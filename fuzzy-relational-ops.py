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
    print("3. Min-Cartesian Product")
    print("4. Inner Product")
    print("5. Outer Product")
    print("6. Complement" )
    print("7. Containment")
    print("8. Exit")
    print("Enter your choice(1-8): ")
    x = int(input())
    if x == 1: 
        x = input("Enter dimensions of relations: ").split()
        n, m = int(x[0]), int(x[1])
        r1 = list(list())
        r2 = list(list())
        print("Enter relation 1: ")
        for i in range(n):
            x = list()
            for j in range(m):
                a = float(input())
                x.append(a)
            r1.append(x)
        print("Enter relation 2: ")
        for i in range(n):
            x = list()
            for j in range(m):
                a = float(input())
                x.append(a)
            r2.append(x)
        r1 = np.array(r1)
        r2 = np.array(r2)
        print ("R1oR2 => Max-Min :\n" + str(maxMin(r1, r2)) + "\n")
    elif x == 2:
        x = input("Enter dimensions of relations: ").split()
        n, m = int(x[0]), int(x[1])
        r1 = list(list())
        r2 = list(list())
        print("Enter relation 1: ")
        for i in range(n):
            x = list()
            for j in range(m):
                a = float(input())
                x.append(a)
            r1.append(x)
        print("Enter relation 2: ")
        for i in range(n):
            x = list()
            for j in range(m):
                a = float(input())
                x.append(a)
            r2.append(x)
        r1 = np.array(r1)
        r2 = np.array(r2)
        print ("R1oR2 => Max-Product :\n" + str(maxProduct(r1, r2)) + "\n\n")
    elif x == 3:
        x = input("Enter dimensions of relations: ").split()
        n, m = int(x[0]), int(x[1])
        r1 = list(list())
        r2 = list(list())
        print("Enter relation 1: ")
        for i in range(n):
            x = list()
            for j in range(m):
                a = float(input())
                x.append(a)
            r1.append(x)
        print("Enter relation 2: ")
        for i in range(n):
            x = list()
            for j in range(m):
                a = float(input())
                x.append(a)
            r2.append(x)
        r1 = np.array(r1)
        r2 = np.array(r2)
        print ("R1oR2 => Min-Cartesian-Product: \n: " + str(cartprod(r1,r2)))
    elif x == 4:
        #take input
        x = input("Enter dimensions of relations: ").split()
        n, m = int(x[0]), int(x[1])
        r1 = list(list())
        r2 = list(list())
        print("Enter relation 1: ")
        for i in range(n):
            x = list()
            for j in range(m):
                a = float(input())
                x.append(a)
            r1.append(x)
        print("Enter relation 2: ")
        for i in range(n):
            x = list()
            for j in range(m):
                a = float(input())
                x.append(a)
            r2.append(x)
        r1 = np.array(r1)
        r2 = np.array(r2)
        print ("R1oR2 => Inner-Product: \n: " + str(inner_product(r1,r2)))
    elif x == 5:
        #take input
        x = input("Enter dimensions of relations: ").split()
        n, m = int(x[0]), int(x[1])
        r1 = list(list())
        r2 = list(list())
        print("Enter relation 1: ")
        for i in range(n):
            x = list()
            for j in range(m):
                a = float(input())
                x.append(a)
            r1.append(x)
        print("Enter relation 2: ")
        for i in range(n):
            x = list()
            for j in range(m):
                a = float(input())
                x.append(a)
            r2.append(x)
        r1 = np.array(r1)
        r2 = np.array(r2)
        print ("R1oR2 => Outer-Product: \n: " + str(outer_product(r1,r2)))
    elif x == 6:
        #take input
        x = input("Enter dimensions of relations: ").split()
        n, m = int(x[0]), int(x[1])
        r1 = list(list())
        print("Enter relation 1: ")
        for i in range(n):
            x = list()
            for j in range(m):
                a = float(input())
                x.append(round(1-a,2))
            r1.append(x)
        r1 = np.array(r1)
        print ("R1 => Complement: \n: " + str(r1))
    elif x == 7:
        x = input("Enter dimensions of relations: ").split()
        n, m = int(x[0]), int(x[1])
        r1 = list(list())
        r2 = list(list())
        print("Enter relation 1: ")
        for i in range(n):
            x = list()
            for j in range(m):
                a = float(input())
                x.append(a)
            r1.append(x)
        print("Enter relation 2: ")
        for i in range(n):
            x = list()
            for j in range(m):
                a = float(input())
                x.append(a)
            r2.append(x)
        r3 = list(list())
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
    elif x == 8:
        return
    menu()
    
if __name__ == '__main__':
    main()
