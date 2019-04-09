# A collection of useful functions
#
# NumpyUtility.py
#
# Paul Grimes, 2018


import numpy as np


def findNearestIdx(array, value):
    '''Return the index of nearest value in an array to the given value'''
    idx = (np.abs(array-value)).argmin()
    return idx

def findNearest(array, value):
    '''Return the nearest value in an array to the given value'''
    try:
        nearest = array[findNearestIdx(array, value)]
    except IndexError:
        nearest = np.asscalar(array)
    return nearest