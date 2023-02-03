#!/usr/bin/python3

def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    result = (list(filter(lambda x: x % 2 == 0, range(n+1))))
    return result
