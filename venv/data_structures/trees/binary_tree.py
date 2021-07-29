from constants import *
from node import Node, State
from stack import Stack


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)


if __name__ == MAIN:
    print('hello')
    state = State(10)
    state.set_visited_right()
    print(state)
