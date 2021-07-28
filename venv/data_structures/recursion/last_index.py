"""
Problem statement
Given an array arr and a target element target, find the last index of occurence of target in arr using recursion. If target is not present in arr, return -1.

For example:

For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 5, output = 6

For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 7, output = -1
"""

MAIN = '__main__'


def last_index(l, t):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    TODO: complete this method to find the last index of target in arr
    """
    if not l:
        return -1
    try:
        i = l.index(t)
        return max(
                    i,
                    i + 1 + last_index(l[i + 1:], t)
                  )
    except ValueError:
        return -1



def test_last_index():
    assert last_index([1, 2, 5, 5, 4], 5) == 3
    assert last_index([1, 2, 5, 5, 4], 7) == -1
    assert last_index([91, 19, 3, 8, 9], 91) == 0
    assert last_index([1, 1, 1, 1, 1, 1], 1) == 5


if __name__ == MAIN:
    test_last_index()