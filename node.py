# node.py

import random

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, node):
        dx = self.x - node.x
        dy = self.y - node.y
        return (dx ** 2 + dy ** 2) ** 0.5

    @staticmethod
    def random_nodes(num_nodes, width, height):
        nodes = []
        for i in range(num_nodes):
            x = random.uniform(0, width)
            y = random.uniform(0, height)
            nodes.append(Node(x, y))
        return nodes
