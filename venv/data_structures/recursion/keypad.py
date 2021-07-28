"""
Keypad Combinations
A keypad on a cellphone has alphabets for all numbers between 2 and 9, as shown in the figure below:



You can make different combinations of alphabets by pressing the numbers.

For example, if you press 23, the following combinations are possible:

ad, ae, af, bd, be, bf, cd, ce, cf

Note that because 2 is pressed before 3, the first letter is always an alphabet on the number 2. Likewise, if the user types 32, the order would be

da, db, dc, ea, eb, ec, fa, fb, fc

Given an integer num, find out all the possible strings that can be made using digits of input num. Return these strings in a list. The order of strings in the list does not matter. However, as stated earlier, the order of letters in a particular string matters.
"""


def get_characters(num):
    if num not in range(10):
        raise ValueError(f'invalid digit {num}')
    chars = [
                '',
                '',     'abc', 'def',
                'ghi',  'jkl', 'mno',
                'pqrs', 'tuv', 'wxyz'
            ]
    return chars[num]


def keypad(num):
    # TODO: Write your keypad solution here!
    if num // 10 == 0:
        return [''] if num == 0 else [char for char in get_characters(num)]

    combinations = list()
    rest = keypad(num // 10)

    for char in get_characters(num % 10):
        combinations += list(map(lambda x: x + char, rest))
    return combinations