"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

from functools import reduce
MAIN, LINEAR, NL, PLOT = '__main__', lambda x: x, '\n', True


# noinspection PyShadowingNames
def get_code(call, calling=True):
    num = call[0] if calling else call[1]
    if num[:3] == '140':
        return num[:3]
    elif num[0:2] == '(0':
        end = num.find(')')
        return num[:end + 1]
    elif num[0] in {'7', '8', '9'}:
        return num.split()[0][:4]
    else:
        raise ValueError('Invalid number')


def get_codes(call):
    return get_code(call, calling=True), \
           get_code(call, calling=False)


def update(code_map, calling, receiving):
    rec_dict = code_map.get(calling, dict())
    count = rec_dict.get(receiving, 0)

    rec_dict[receiving] = count + 1
    code_map[calling] = rec_dict


def get_percent(code_map, code):
    codes = code_map.get(code, dict())
    num = codes.get(code, 0)
    return num * 100 / sum(codes.values())


# noinspection PyShadowingNames
def called_percent(code_map, code):
    called = sorted(list(code_map.get(code, dict()).keys()))
    percent = get_percent(code_map, code)
    return called, percent


# noinspection PyShadowingNames
def solution(size):
    code_map, blr = dict(), '(080)'
    for call in calls[:size]:
        called, received = get_codes(call)
        if called and received:
            update(code_map, called, received)
    return called_percent(code_map, blr)


def time(size):
    from time import time
    start, _, end = time(), solution(size), time()
    return end - start


# noinspection PyShadowingNames
def performance(s=100):
    sizes = range(s, len(calls))
    return sizes, [time(size) for size in sizes]


if __name__ == MAIN:
    called, percentage = solution(len(calls))
    print(f"The numbers called by people in Bangalore have codes: {NL + NL.join(called)}")
    print(f"{percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

    if PLOT:
        from plot import plot
        n, t = performance()
        plot(n, t, loglog=True, interpolation=LINEAR)
