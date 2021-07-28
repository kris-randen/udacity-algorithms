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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

MAIN, LINEAR, NL, PLOT = '__main__', lambda x: x, '\n', True


# noinspection PyShadowingNames
def solution(size_t, size_c):
    texter, textee, time_t = texts[0][0], texts[0][1], texts[0][2]
    caller, callee, time_c, num = calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][-1]
    return (texter, textee, time_t), \
           (caller, callee, time_c, num)


def time(size):
    from time import time
    start, _, end = time(), solution(size, size), time()
    return end - start


def performance(s=100):
    sizes = range(s, len(texts))
    return sizes, [time(size) for size in sizes]


if __name__ == MAIN:
    (texter, textee, time_t), \
    (caller, callee, time_c, num) = solution(len(texts), len(calls))
    print(f"First record of texts, {texter} texts {textee} at time {time_t}")
    print(f"Last record of calls, {caller} calls {callee} at time {time_c}, lasting {num} seconds")

    if PLOT:
        from plot import plot
        n, t = performance()
        plot(n, t, loglog=True, interpolation=LINEAR)

