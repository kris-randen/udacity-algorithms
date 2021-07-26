# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from random import choice as pick
from random import randrange as rrange
from string import ascii_uppercase as asc


def signature(name):
    sign = dict()
    for char in name:
        sign[char] = sign.get(char, 0) + 1
    return sign


def test_signature():
    assert signature('krishnaswami') == {'k': 1, 'r': 1, 'i': 2, 's': 2, 'h': 1, 'n': 1, 'a': 2, 'w': 1, 'm': 1}


def num_instances(name_sign, string_sign):
    min = 10000
    for char, count in name_sign.items():
        num = string_sign.get(char, 0) // name_sign[char]
        if num == 0:
            return 0
        min = num if num < min else min
    return min


def instances(name, string):
    return num_instances(signature(name), signature(string))


def test_num_instances():
    assert num_instances(signature('BILL'), signature('BILLOBILLOLLOBBI')) == 3
    assert num_instances(signature('BOB'), signature('BILLOBILLOLLOBBI')) == 2


def test_instances():
    assert instances('ILOVEMYDOG', 'CAT') == 0
    assert instances('CATS', 'CAT') == 0


def gen_name(size):
    alphabet = asc[:27]
    name = ""
    for _ in range(size):
        name += pick(alphabet)
    return name


def gen_names(k, start=3, end=7):
    names = list()
    for _ in range(k):
        size = rrange(start, end)
        names.append(gen_name(size))


# noinspection PyShadowingNames
def gen_catalog(names, num=5):
    string = ""
    for name in names:
        num_instances = rrange(num)
        string += num_instances*name
    return string


def check_instances(name, S):
    from copy import deepcopy as dp
    max = 0
    S_set = list(S)
    num = 0

    while True:
        print(f"S_set = {S_set}")
        print(f"num = {num}")
        error = False
        for char in name:
            print(f"char = {char}")
            try:
                S_set.remove(char)
                print(f"S_set = {S_set}")
            except KeyError:
                error = True
                break
        if error:
            break
        num += 1
    return num


def solution(S, L):
    # write your code in Python 3.6
    max = 0
    for name in L:
        num = instances(name, S)
        max = num if num > max else max
    return max


if __name__ == '__main__':
    from pprint import pp
    print(f"signature('ILOVEMYDOG') = {signature('ILOVEMYDOG')}")
    # print(f"signature('BILLOBILLOLLOBBI') = {signature('BILLOBILLOLLOBBI')}")
    # test_signature()
    # test_num_instances()
    # test_instances()
    print(gen_name(7))
    assert check_instances('BILL', 'BILLOBILLOLLOBBI') == 3