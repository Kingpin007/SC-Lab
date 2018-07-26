# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:34:42 2018

@author: Kingpin007
Equation: 1/(1+x^2)
"""
import matplotlib.pyplot as plt
from scipy.special import gamma as Gamma
from scipy import signal
from pylab import *

def gamma(x):
    return Gamma(x)

def gauss(x,sigma):
    return signal.gaussian(x,std=sigma)

def triangular(x):
    return signal.triang(x)
    
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
    


if __name__ == '__main__':
    main()


