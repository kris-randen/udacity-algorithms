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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

MAIN, LINEAR, NL, PLOT = '__main__', lambda x: x, '\n', True


# noinspection PyShadowingNames
def solution(size_t, size_c):
    nums = set()
    for text in texts[:size_t]:
        nums.update([text[0], text[1]])
    for call in calls[:size_c]:
        nums.update([call[0], call[1]])
    return len(nums)


def time(size):
    from time import time
    start, _, end = time(), solution(size, size), time()
    return end - start


# noinspection PyShadowingNames
def performance(s=100):
    sizes = range(s, min(len(texts), len(calls)))
    return sizes, [time(size) for size in sizes]


if __name__ == MAIN:
    count = solution(size_t=len(texts), size_c=len(calls))
    print(f"There are {count} different telephone numbers in the records.")

    if PLOT:
        from plot import plot
        n, t = performance()
        plot(n, t, loglog=True, interpolation=LINEAR)