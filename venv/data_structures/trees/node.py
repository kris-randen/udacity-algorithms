from constants import *


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self, value):
        self.left = Node(value)

    def set_right_child(self, value):
        self.right = Node(value)


    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None


    def __repr__(self):
        return f'Node: value = {self.get_value()}'


class State:
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True


    def __str__(self):
        s = 'Node = ' + str(self.node)
        s += '\n-------------\n'
        s += 'left = ' + ('' if self.get_visited_left() else 'not ') + 'visited'
        s += '\n-------------\n'
        s += 'right = ' + ('' if self.get_visited_right() else 'not ') + 'visited'
        s += '\n-------------\n'
        return s

    def __repr__(self):
        return self.__str__()


if __name__ == MAIN:
    state = State(10)
    state.set_visited_right()
    print(state)
