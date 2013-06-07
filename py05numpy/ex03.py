#!/usr/bin/env python

import numpy
import numpy as np

'''Ex3, random and statistics

Task1: generate random numbers
Task2: calculate mean/std/var of data
Task3: calculate mean/std/var of data along specific axis
'''

'''Task1: generate random numbers
Use numpy.sin() to create an ndarray of 2 periods and 1000 data points.

Use numpy.random.randn() to generate an ndarray of noise with 1000 data 
points (normally distributed). The normal distribution of the noise should have
a median of A0 (your choice, keep it single digits), and a standard deviation
10% of the sine wave amplitude. Add these together into a new ndarray. 
''' 
def task1():
    return

'''Task2: calculate mean/std/var of data
 
using random data generated in task(), calculate their mean, standard deviation,
variance, median.
'''
def task2(y):
    '''y is data generated in task1
    '''
    return

'''Task3: calculate mean/std/var of data along specific axis

First reshape the date generated in task to to (10,100). Then calculate mean,
std, var along first and second axis by adding keywords 'axis' to those
functions. 
'''
def task3(y):
    '''y is data generated in task1
    '''
    return

if __name__=='__main__':
    task1()
    task2()
    task3()
    