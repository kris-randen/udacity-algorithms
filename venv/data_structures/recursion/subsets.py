"""
Problem Statement
Given an integer array, find and return all the subsets of the array. The order of subsets in the output array is not important. However the order of elements in a particular subset should remain the same as in the input array.

Note:

An empty set will be represented by an empty list.
If there are repeat integers, each occurrence must be treated as a separate entity.
Example 1

arr = [9, 9]

output = [[],
          [9],
          [9],
          [9, 9]]
Example 2

arr = [9, 12, 15]

output =  [[],
           [15],
           [12],
           [12, 15],
           [9],
           [9, 15],
           [9, 12],
           [9, 12, 15]]
"""

from functools import reduce

MAIN, NL = '__main__', '\n'


def subsets(l):
    """
    :param: arr - input integer array
    Return - list of lists (two dimensional array) where each list represents a subset
    TODO: complete this method to return subsets of an array
    """
    if not l:
        return [[]]
    first, rest = l[0], subsets(l[1:])
    return sorted(
                    [sub for sub in rest] +
                    [[first] + sub for sub in rest], key=len
                 )


if __name__ == MAIN:
    print(subsets([9, 12, 15]))
