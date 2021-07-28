"""
Problem Statement
The Tower of Hanoi is a puzzle where we have three rods and n unique sized disks. The three rods are - source, destination, and auxiliary as shown in the figure below.

Initally, all the n disks are present on the source rod. The final objective of the puzzle is to move all disks from the source rod to the destination rod using the auxiliary rod.

However, there are some rules applicable to all rods:

1. Only one disk can be moved at a time.
2. A disk can be moved only if it is on the top of a rod.
3. No disk can be placed on the top of a smaller disk.
You will be given the number of disks num_disks as the input parameter. Write a recursive function tower_of_Hanoi() that prints the "move" steps in order to move num_disks number of disks from Source to Destination using the help of Auxiliary rod.v
"""


MAIN, NL = '__main__', '\n'


def transfer(k, s, d):
    print(f"{s} {d}")


def move(n, s, d, a):
    if n == 1:
        transfer(n, s, d)
        return
    move(n-1, s, a, d)
    transfer(n, s, d)
    move(n-1, a, d, s)


def tower_of_Hanoi(n):
    """
    :param: num_disks - number of disks
    TODO: print the steps required to move all disks from source to destination
    """
    
    move(n, 'S', 'D', 'A')


def print_sol(n):
    print('-----------------------------')
    print(f'Tower of Hanoi {n}')
    print('-----------------------------')
    tower_of_Hanoi(n)


if __name__ == MAIN:
    print_sol(2)
    print_sol(3)
    print_sol(4)
