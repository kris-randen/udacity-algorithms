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


# noinspection PyShadowingNames
def solution(size_texts, size_calls):
    nums = set()
    for text in texts[:size_texts]:
        nums.update([text[0], text[1]])
    for call in calls[:size_calls]:
        nums.update([call[0], call[1]])
    return nums


# noinspection PyShadowingNames
def performance():
    from time import time

    min_size = min(len(texts), len(calls))
    sizes = range(80, min_size)
    times = list()

    for size in sizes:
        start = time()
        nums = solution(size, size)
        end = time()
        times.append(end - start)
    return sizes, times


if __name__ == '__main__':
    from plot import plot

    nums = solution(size_texts=len(texts), size_calls=len(calls))
    print(f"There are {len(nums)} different telephone numbers in the records.")
    n, t = performance()
    plot(n, t, loglog=True, interpolation=lambda x: x)

    #The runtime complexity is O(n)