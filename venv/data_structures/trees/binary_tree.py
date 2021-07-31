from constants import *
from node import Node
from stack import Stack
from collections import deque
from copy import deepcopy


class BinaryTree:
    # noinspection PyShadowingNames
    def __init__(self, values):
        self.root = BinaryTree.construct_preorder(values)

    def get_root(self):
        return self.root

    # noinspection PyShadowingNames
    @staticmethod
    def construct_preorder(values):
        if not values or not values[0]:
            return None
        node = Node(values[0])
        values.popleft()
        node.left = BinaryTree.construct_preorder(values)
        values.popleft()
        node.right = BinaryTree.construct_preorder(values)
        return node


# noinspection PyShadowingNames
class Visitor:

    def __init__(self):
        self.visit_order = deque()

    def get_visit_order(self):
        return deepcopy(self.visit_order)

    def update_order(self, node, visit=True):
        self.visit_order.append(node.get_value())

    def visit(self, node):
        node.set_visited()
        self.update_order(node)

    def refresh(self):
        self.visit_order.clear()


# noinspection PyShadowingNames
def traverse_preorder_stack(tree, visitor):
    stack = Stack()
    node = tree.get_root()
    visitor.visit(node)
    stack.push(node)
    while stack.top():
        node = stack.top()
        if node.get_left() and not node.get_left_visited():
            left = node.get_left()
            visitor.visit(left)
            stack.push(left)
        elif node.get_right() and not node.get_right_visited():
            right = node.get_right()
            visitor.visit(right)
            stack.push(right)
        else:
            stack.pop()
    return visitor.get_visit_order()


# noinspection PyShadowingNames
def traverse_preorder_recursive(tree, visitor):
    pass


if __name__ == MAIN:
    values = deque(['apple', 'banana', 'dates', None, None, None, 'cherry', None, None])
    tree = BinaryTree(values)
    visitor = Visitor()
    traverse_preorder_stack(tree, visitor)
    visit_order = visitor.get_visit_order()
    print(visit_order)



