# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from functools import reduce
from operator import add


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def valid(board, p):
    h, w = len(board), len(board[0])
    if p[0] < 0 or p[0] >= h or p[1] < 0 or p[1] >= w:
        return False
    if board[p[0]][p[1]] == '#':
        return False
    return True


# noinspection PyShadowingNames
def convert(char):
    moves = dict(U=(-1, 0), D=(1, 0), L=(0, -1), R=(0, 1))
    return moves.get(char, None)


def get_next(move, point):
    return add(convert(move), point)


def do_move(board, move, start):
    end = get_next(move, start)
    return end if valid(board, end) else start


def solution(board, moves):
    return reduce(lambda p, q: add(p, do_move(board, p, q)), moves, (0, 0))
    # position = (0, 0)
    # for move in moves:
    #     position = do_move(board, move, position)
    # return position


if __name__ == '__main__':
    print(solution(['.#.', '..#'], 'DLRR'))