def deep_reverse(v):
    from copy import deepcopy as dp

    if not isinstance(v, list):
        return dp(v)

    if len(v) == 0:
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