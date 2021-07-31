from constants import *


class Node:
    def __init__(self, value=None):
        self.value = value
        self.visited = False
        self.left = None
        self.right = None

    def get_visited(self):
        return self.visited

    def set_visited(self, visited=True):
        self.visited = visited

    def get_left_visited(self):
        left = self.get_left()
        return left.get_visited() if left else None

    def get_right_visited(self):
        right = self.get_right()
        return right.get_visited() if right else None


    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, value):
        self.left = Node(value)

    def set_right(self, value):
        self.right = Node(value)


    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None


    def __repr__(self):
        return f'{self.get_value()}'


if __name__ == MAIN:
    pass
