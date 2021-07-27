def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    # TODO: Write your keypad solution here!

    if num // 10 == 0:
        return [''] if num == 0 else [char for char in get_characters(num)]

    combinations = list()
    rest = keypad(num // 10)
    
    for char in get_characters(num % 10):
        combinations += list(map(lambda x: x + char, rest))
    return combinations