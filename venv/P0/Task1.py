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

if __name__ == '__main__':
    nums = set()
    for text in texts:
        nums.update([text[0], text[1]])
    for call in calls:
        nums.update([call[0], call[1]])
    print(f"There are {len(nums)} different telephone numbers in the records.")