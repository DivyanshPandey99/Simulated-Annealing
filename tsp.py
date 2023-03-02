# tsp.py

import random
import math


class TSP:
    def __init__(self, nodes, temp=10000, cooling=0.997):
        self.nodes = nodes
        self.num_nodes = len(nodes)
        self.temperature = temp
        self.cooling_rate = cooling

        self.current_order = list(range(self.num_nodes))
        self.best_order = list(range(self.num_nodes))
        random.shuffle(self.current_order)
        self.best_distance = self.get_distance(self.current_order)

    def get_distance(self, order):
        """Calculates the total distance traveled for a given order of nodes."""
        distance = 0
        for i in range(self.num_nodes - 1):
            node1 = self.nodes[order[i]]
            node2 = self.nodes[order[i + 1]]
            distance += math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)
        node1 = self.nodes[order[-1]]
        node2 = self.nodes[order[0]]
        distance += math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)
        return distance

    def get_best(self):
        """Returns the best order found so far and its corresponding distance."""
        return self.best_order, self.best_distance

    def anneal(self):
        """Runs the simulated annealing algorithm for a single iteration."""
        # Pick two random nodes to swap
        i = random.randint(0, self.num_nodes - 1)
        j = random.randint(0, self.num_nodes - 1)
        while i == j:
            j = random.randint(0, self.num_nodes - 1)

        # Swap the nodes
        new_order = self.current_order.copy()
        new_order[i], new_order[j] = new_order[j], new_order[i]

        # Calculate the energy (distance) of the new order
        new_distance = self.get_distance(new_order)

        # Calculate the change in energy and determine if we should accept the new order
        delta = new_distance - self.best_distance
        if delta < 0 or random.random() < math.exp(-delta / self.temperature):
            self.current_order = new_order
            self.best_distance = new_distance

            # If this is the best order we've seen, save it
            if self.best_distance < self.get_distance(self.best_order):
                self.best_order = self.current_order

        # Decrease the temperature
        self.temperature *= self.cooling_rate

        # Check if we have converged
        if self.temperature < 1e-6:
            return self.best_distance
