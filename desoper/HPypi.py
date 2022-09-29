#!/usr/bin/env python3
r'''
Hello moduleHPypi module
'''
import dask.array as da
import numpy as np
#import random
#import itertools
#from itertools import permutations

#def hello():
#    r'''
#    Hello function
#    '''
#    return 'Hello, World!'

def valor_m(n):
    """
    valor_m muestra el la cantidad de L y K que se produciran 
    """
    if n%2==0:
        m = n/2 -1
    else:
        m = (n-3)/2
    return m



    
#if __name__ == '__main__':
#    r'''
#    Hello main
#    '''
#    hello()
