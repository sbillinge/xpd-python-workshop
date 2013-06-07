#!/usr/bin/env python

import numpy
import numpy as np

'''this exercise is generally focusing on Broadcasting, element-wise operations,
slices, and ranges. You can write your script here then run it. It is better to
using a interactive shell, Ipython for example to do the task and see the
results immediately.

If you are using interactive shell like Ipython, you should first run this
script using %run command (In [x]: %run ex02.py). Then the example array
s1,s2,s3 will be available in your shell.
'''

s1 = np.array([1,4,9,16,25])
s2 = np.array([[1,2,3,4,5],
               [1,4,9,16,25],
               [1,8,27,64,125]])

'''Task1 Add s1 and s2 to observe broadcasting.
'''
def task1():
    return

'''Get the second value from s1.
'''
def task2():
    return    

'''Get the third row from s2.
'''
def task3():
    return

'''Get the second column from s2.
'''
def task4():
    return

'''Generate a range of values from 1 to 20 in 0.5 step increments.
'''
def task5():
    return

'''Generate a range of values from 5 to 30 with a total of 50 entries.
'''
def task6():
    return

'''Use the np.log10() function to get the log values of ranges obtained from 
task5 and task6 
'''
def task7(x5, x6):
    '''
    x5: range got from task5
    x6: range got from task6
    '''
    return


if __name__ == '__main__':
    print task1()
    print task2()
    print task3()
    print task4()
    print task5()
    print task6()
    print task7()
    
