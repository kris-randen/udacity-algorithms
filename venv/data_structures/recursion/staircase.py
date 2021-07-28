"""
Problem Statement
Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps. In how many possible ways can you climb the staircase if the staircase has n steps? Write a recursive function to solve the problem.

Example:

n == 1 then answer = 1

n == 3 then answer = 4
The output is 4 because there are four ways we can climb the staircase:

1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step
3 steps
n == 5 then answer = 13
"""

MAIN = '__main__'


def staircase(n):
    if n <= 1:
        return 1 if n >= 0 else 0
    return staircase(n-1) + staircase(n-2) + staircase(n-3)


if __name__ == MAIN:
    print(staircase(1))
    print(staircase(3))
    print(staircase(4))
    print(staircase(7))