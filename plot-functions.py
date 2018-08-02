# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:34:42 2018

@author: Kingpin007
Equation: 1/(1+x^2)
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma as Gamma
from scipy import signal
from scipy.integrate import simps, trapz
from pylab import *

def f(x):
    return x**2

def gamma(x):
    return Gamma(x)

def gauss(x,sigma):
    return signal.gaussian(x,std=sigma)

def triangular(x):
    return signal.triang(x)

def trapezoidal(f, a, b, n):
    h = float(b - a) / n
    s = 0.0
    s += f(a)/2.0
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s * h

def sigmoid(x):
    a = []
    for item in x:
                      #(the sigmoid function)
        a.append(1/(1+math.exp(-item)))
    return a

    
def main():
    x = linspace(-6, 6, 1024)
    y1 = gamma(x)
    plot(x, y1)
    xlabel('x')
    ylabel('y')
    axis([-6, 6, -100, 100])
    grid(True)
    show()
    window = gauss(51,7)
    plt.plot(window)
    plt.title(r"Gaussian window ($\sigma$=7)")
    plt.ylabel("Amplitude")
    plt.xlabel("Sample")
    plt.show()
    window = triangular(51)
    plt.plot(window)
    plt.title("Triangular window")
    plt.ylabel("Amplitude")
    plt.xlabel("Sample")
    plt.show()
    mu, sigma = 0, 0.1 # mean and standard deviation
    s = np.random.normal(mu, sigma, 1000)
    count, bins, ignored = plt.hist(s, 30, normed=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
    plt.title("Bell Curve")
    plt.show()
    fig, ax = plt.subplots(1,1)
    x=np.arange(0,9,0.01)
    y=f(x)
    ax.plot(y,x, 'k-')
    xstep = np.arange(0,10,3)
    area=trapz(y,x)
    print( area)
    ax.fill_between(f(xstep), 0, xstep)
    plt.title("Trapeziodal window")
    plt.show()
    x = np.arange(-10., 10., 0.1)
    y = sigmoid(x)
    plt.plot(x,y)
    plt.title("s funtion window")
    plt.show()


if __name__ == '__main__':
    main()


