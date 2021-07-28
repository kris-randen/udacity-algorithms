"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

MAIN, LINEAR, NL, PLOT = '__main__', lambda x: x, '\n', True


# noinspection PyShadowingNames
def increment_single(times, key, time):
    times[key] = times.get(key, 0) + time


def increment(times, keys, value):
    for key in keys:
        increment_single(times, key, value)


def max_item(times):
    from functools import reduce
    return reduce(lambda x, y: x if x[1] > y[1] else y, times.items())


# noinspection PyShadowingNames
def solution(size):
    times = dict()
    for call in calls[:size]:
        caller, callee, time = call[0], call[1], int(call[-1])
        increment(times, keys=[caller, callee], value=time)
    return max_item(times)


def time(size):
    from time import time
    start, _, end = time(), solution(size), time()
    return end - start


# noinspection PyShadowingNames
def performance(s=100):
    sizes = range(s, len(calls))
    return sizes, [time(size) for size in sizes]


if __name__ == MAIN:
    num, max = solution(len(calls))
    print(f"{num} spent the longest time, {max} seconds, on the phone during September 2016.")

    if PLOT:
        from plot import plot
        n, t = performance()
        plot(n, t, loglog=True, interpolation=LINEAR)