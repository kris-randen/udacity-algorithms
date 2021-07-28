"""
Problem Statement
Define a procedure, deep_reverse, that takes as input a list, and returns a new list that is the deep reverse of the input list.
This means it reverses all the elements in the list, and if any of those elements are lists themselves, reverses all the elements in the inner list, all the way down.

Note: The procedure must not change the input list itself.

Example
Input: [1, 2, [3, 4, 5], 4, 5]
Output: [5, 4, [5, 4, 3], 2, 1]

Hint

Begin with a blank final list to be returned.
Traverse the given list in the reverse order.
If an item in the list is a list itself, call the same function.
Otheriwse, append the item to the final list.
"""


def deep_reverse(v):
    from copy import deepcopy as dp

    if not isinstance(v, list):
        return dp(v)

    if not v:
        return []

    return [deep_reverse(v[-1])] + deep_reverse(v[:-1])


def test_function(t):
    print(f"{'Pass' if deep_reverse(t[0]) == t[1] else 'Fail'}")


def test_deep_reverse():
    test_function([
                    [1, 2, 3, 4, 5],
                    [5, 4, 3, 2, 1]
                  ])

    test_function([
                    [1, 2, [3, 4, 5], 4, 5],
                    [5, 4, [5, 4, 3], 2, 1]
                  ])

    test_function([
                    [1, [2, 3, [4, [5, 6]]]],
                    [[[[6, 5], 4], 3, 2], 1]
                  ])

    test_function([
                    [[[[]]], [[]]],
                    [[[]], [[[]]]]
                  ])


if __name__ == '__main__':
    test_deep_reverse()