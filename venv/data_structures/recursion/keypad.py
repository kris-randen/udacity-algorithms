def get_characters(num):
    if not 0 <= num <= 9:
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