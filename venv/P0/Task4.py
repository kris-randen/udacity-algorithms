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

if __name__ == '__main__':
    nums_making_calls = set()
    nums_receiving_calls = set()
    for call in calls:
        nums_making_calls.add(call[0])
        nums_receiving_calls.add(call[1])

    nums_sending_texts = set()
    nums_receiving_texts = set()
    for text in texts:
        nums_sending_texts.add(text[0])
        nums_receiving_texts.add(text[1])

    non_telemarketers = nums_sending_texts.union(nums_receiving_texts).union(nums_receiving_calls)
    telemarketers = nums_making_calls.difference(non_telemarketers)
    nl = '\n'
    print(f"These numbers could be telemarketers: {nl + nl.join(list(telemarketers))}")