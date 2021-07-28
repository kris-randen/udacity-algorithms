"""
Problem Statement
Given an input string, return all permutations of the string in an array.

Example 1:

string = 'ab'
output = ['ab', 'ba']
Example 2:

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
"""

from constants import *


def permute(s):
    if len(s) < 2:
        return [s]
    perm = []
    for i in range(len(s)):
        q = s[i] + s[:i] + s[i+1:]
        perm += list(map(lambda x: q[0] + x, permute(q[1:])))
    return perm


def test_permute():
    from permute import check

    print("Pass" if (check(permute('ab'),
                           ['ab', 'ba'])) else "Fail")
    print("Pass" if (check(permute('abc'),
                           ['abc', 'bac', 'bca', 'acb', 'cab', 'cba'])) else "Fail")
    print("Pass" if (check(permute('abcd'),
                           ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba'])) else "Fail")


if __name__ == MAIN:
    test_permute()