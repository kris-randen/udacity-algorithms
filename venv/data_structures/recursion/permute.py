"""
Permutation
Question - Let's use recursion to help us solve the following permutation problem:

Given a list of items, the goal is to find all of the permutations of that list. For example,
Given a list like: [0, 1, 2]
Permutations: [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

Notice that the expected output is a list of permutation with each permuted item being represented by a list. Such an object that contains other object is called "compound" object.
"""
MAIN = '__main__'

from copy import deepcopy as dp
from operator import add


def permute(l):
    """
    Args: myList: list of items to be permuted
    Returns: list of permutation with each permuted item being represented by a list
    """
    if not l:
        return [[]]
    q, perm = dp(l), []
    for i in range(len(q)):
        q[0], q[i] = q[i], q[0]
        perm += list(
                    map(
                        lambda x: [q[0]] + x, permute(q[1:])
                       )
                    )
    return perm


def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.

    Note that the ordering of the list is not important.

    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list

    Returns:
        bool
    """
    o = dp(output)  # so that we don't mutate input
    e = dp(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    return o == e


if __name__ == MAIN:
    print("Pass" if (check_output(permute([]), [[]])) else "Fail")
    print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
    print("Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
    print("Pass" if (check_output(permute([0, 1, 2]),
                                  [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")