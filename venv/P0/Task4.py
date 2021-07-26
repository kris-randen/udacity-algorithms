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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


# noinspection PyShadowingNames
def solution(size_calls, size_texts):
    nums_making_calls = set()
    nums_receiving_calls = set()
    for call in calls[:size_calls]:
        nums_making_calls.add(call[0])
        nums_receiving_calls.add(call[1])

    nums_sending_texts = set()
    nums_receiving_texts = set()
    for text in texts[:size_texts]:
        nums_sending_texts.add(text[0])
        nums_receiving_texts.add(text[1])

    non_telemarketers = nums_sending_texts.union(nums_receiving_texts).union(nums_receiving_calls)
    telemarketers = nums_making_calls.difference(non_telemarketers)
    return telemarketers


# noinspection PyShadowingNames
def performance():
    from time import time

    sizes = range(100, min(len(calls), len(texts)))
    times = list()

    for size in sizes:
        start = time()
        telemarketers = solution(size, size)
        end = time()
        times.append(end - start)

    return sizes, times


if __name__ == '__main__':
    from plot import plot

    telemarketers = solution(len(calls), len(texts))
    nl = '\n'
    print(f"These numbers could be telemarketers: {nl + nl.join(list(telemarketers))}")

    n, t = performance()
    plot(n, t, True, lambda x: x)

    #The runtime complexity is O(n)