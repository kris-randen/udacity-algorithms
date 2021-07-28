"""
Problem statement
In an encryption system where ASCII lower case letters represent numbers in the pattern a=1, b=2, c=3... and so on, find out all the codes that are possible for a given input number.

Example 1

number = 123
codes_possible = ["aw", "abc", "lc"]
Explanation: The codes are for the following number:

1 . 23 = "aw"
1 . 2 . 3 = "abc"
12 . 3 = "lc"
Example 2

number = 145
codes_possible = ["ade", "ne"]
Return the codes in a list. The order of codes in the list is not important.

Note: you can assume that the input number will not contain any 0s
"""

from functools import reduce

MAIN, NL = '__main__', '\n'


def code(char):
    return get_code(int(char))


def codes(chars):
    return ''.join(code(char) for char in chars if code(char))


# noinspection PyShadowingNames
def get_code(num):
    from string import ascii_lowercase
    n = 26
    codes = {asci: char for asci, char in
             zip(range(1, n+1), ascii_lowercase[:n])}
    return codes.get(num, None)


def prefix(first, token):
    token[0] = first + token[0]
    return token


def append(first, token):
    return [first] + token


# noinspection PyShadowingNames
def get_tokens(chars):
    if len(chars) < 2:
        return [chars]

    first, tokens = chars[0], get_tokens(chars[1:])
    return [append(first, token) for token in tokens] + \
           [prefix(first, token) for token in tokens]


# noinspection PyShadowingNames
def all_codes(num):
    """
    :param: number - input integer
    Return - list() of all codes possible for this number
    TODO: complete this method and return a list with all possible codes for the input number
    """

    tokens = get_tokens(list(str(num)))
    return {codes(token) for token in tokens if codes(token)}


if __name__ == MAIN:
    print(all_codes(100023))