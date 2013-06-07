#!/usr/bin/env python

import numpy
import numpy as np

'''ex4: interpolation and polynomial fitting

Task1: comparing 2 datasets on different x-grid using interpolation
Task2: fit a polynomial function to a set of data
'''

'''Task1: comparing 2 datasets on different x-grid using interpolation

First you need to generate two x-grids with different interval, using np.arange,
np.linespace or np.logspace. For example, x1, x2

Then calculate two y array using different x-grids using any functions you like.
For example y1 = np.sin(x1), y2 = np.sin(x2)

Then interpolate one y1 onto grid x2 using numpy.interp()
Or you can scipy.interpolate which is more powerful interpolate

return x1, x2, y1, y2, y1interpolated
'''

def task1():
    '''return a list of array [x1, x2, y1, y2, y1interplated]
    '''
    return

'''Task2: fit a polynomial function to a set of data

First you need to generate data sets you want to fit. For example:
x = np.arange(0, 10, 0.01)
y = np.exp(x)

Then you can fit the data sets using a polynomial functions using numpy.polyfit
You can specify the degree of fitting polynomial

You can evaluate the fitting functions using numpy.polyval

return data sets x,y and fitted functions evaluated at grid x, (x,y,yfit)
'''
def task2():
    '''return a list of array [x,y,yfit]
    '''
    return

def main():
    x1, x2, y1, y2, y1i = task1()
    import matplotlib.pyplot as plt
    plt.figure(1)
    plt.plot(x1, y1, label='x1-y1')
    plt.plot(x2, y2, label='x2-y2')
    plt.plot(x2, y1i, label='x2-y1_interpolated')
    plt.legend()
    
    xx, yy, yyfit = task2()
    plt.figure(2)
    plt.plot(xx, yy, label='data set')
    plt.plot(xx, yyfit, label = 'fitted function')
    plt.legend()
    
    plt.show()
    return

if __name__=='__main__':
    main()