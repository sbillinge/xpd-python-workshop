#!/usr/bin/env python

import numpy
import numpy as np

"""
ex1, load the save array using numpy

Task1, load the 3 column data from a .txt file using numpy.loadtxt
Task2, save 3 array into a 3 column format .txt file
Task3, load and save the 2D array from a .npy data

Please look up the online documents to find the usage of each functions.

To run this functions, you can run this script in a terminal
or you can import these functions to a python shell and run them.
"""

'''Task1, load the 3 column data from a .txt file using numpy.loadtxt

The ex1.txt is a 3 column data file. Loading the data from it using
numpy.loadtxt function and return a 2D array 'rv'. The shape of 2D array should
be [3, n], where n is the length of the data. So you can access the x column by
rv[x]. 

You may use transpose() function/method to transpose the 2d array, or unpack
keywords in numpy.loadtxt function.
'''
def task1():
    '''docstrings for task1
    '''
    #load data from ex1.txt using numpy.loadtxt
    
    return

'''Task2, save 3 array into a 3 column format .txt file

Assume you finish your data process and want to save the results to a file. You
have 3 array to save, which is x, y, and dy. The data file saved in disk should
have 3 column format, i.e. x,y,dy in each line of the file and there are n lines
in total. 

To do so the actual array you saved should be in shape of [3,n]. You may use
numpy.transpose() function. to transpose the 2D array.
'''

def task2(filename):
    '''docstrings for task2
    '''
    # generate x,y,dy, you may generate your own x,y,dy
    x = np.arange(0,10,0.01)
    y = np.sin(x)
    dy = np.random.random(len(x))
    # save x,y,dy into a 3 column data file
    # FIXME ... fix the data variable below
    data = [1]
    np.savetxt(filename, data)
    return

'''Task3, load and save the 2D array from a .npy data

You can also save/load ndarray using binary format .npy, which is only
accessable by numpy The ex3.npy is a .npy file which contains a 100*100 array.
You can use numpy.load to load the array from this file. Then do some process
and save it in the save format using numpy.save .
'''

def task3():
    '''docstrings for task3
    '''
    #load data in ex3.npy to a variable, a for example, using numpy.load
    
    #do some process, for example a = a*20
    
    #save a to a file, ex3_1.npy for example, using numpy.save.
    
    #load data in ex3_1.npy to a variable, b for example, using numpy.load
    
    #test if b is equal to a by using
    #if numpy.array_equal(a, b):
    #    print 'Great! arrays a and b are equal!'
    #else:
    #    print 'Oh, there is something wrong, a and b differ.'
    
    return


def main():
    '''Do simple shape check on task1.
    For task2, please open .txt file you saved to see if it is right
    For task3, please include simple test in function, as test in comments
    '''
    #check task1
    rv = task1()
    if rv.shape == (3, 1000):
        print 'Task1 success!'
    else:
        print 'Please check the shape of array returned in task1()'
        
    task2('task2_out.txt')
    task2_data = np.loadtxt('task2_out.txt')
    if task2_data.shape == (3, 1000):
        print 'Task2 success!'
    else:
        print 'Please check the shape of the data in "task2_out.txt" file'
    
    task3()
    return

if __name__ == '__main__':
    main()
