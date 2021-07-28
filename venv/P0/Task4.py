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

MAIN, LINEAR, NL, PLOT = '__main__', lambda x: x, '\n', True


def senders_receivers(items, size):
    senders, receivers = set(), set()
    for item in items[:size]:
        senders.add(item[0])
        receivers.add(item[1])
    return senders, receivers


def callers_callees(size):
    return senders_receivers(calls, size)


def texters_textees(size):
    return senders_receivers(texts, size)


# noinspection PyShadowingNames
def solution(size_calls, size_texts):
    callers, callees = callers_callees(size_calls)
    texters, textees = texters_textees(size_texts)
    return sorted(list(callers - set().union(texters, textees, callees)))


def time(size):
    from time import time
    start, _, end = time(), solution(size, size), time()
    return end - start


# noinspection PyShadowingNames
def performance(s=100):
    sizes = range(s, min(len(calls), len(texts)))
    return sizes, [time(size) for size in sizes]


if __name__ == MAIN:
    marketers = solution(len(calls), len(texts))
    print(f"These numbers could be telemarketers: {NL + NL.join(list(marketers))}")

    if PLOT:
        from plot import plot
        n, t = performance()
        plot(n, t, loglog=True, interpolation=LINEAR)