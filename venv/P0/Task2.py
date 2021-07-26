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

if __name__ == '__main__':
    from functools import reduce

    times = dict()
    for call in calls:
        time = int(call[-1])
        times[call[0]] = times.get(call[0], 0) + time
        times[call[1]] = times.get(call[1], 0) + time
    max = reduce(lambda x, y: x if x[1] > y[1] else y, times.items())
    print(f"{max[0]} spent the longest time, {max[1]} seconds, on the phone during September 2016.")

