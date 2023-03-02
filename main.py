# main.py

import pygame
import sys

from node import Node
from tsp import TSP


# Constants
WIDTH = 800
HEIGHT = 600
FPS = 1000
NODE_RADIUS = 5
LINE_WIDTH = 2
FONT_SIZE = 30
ITER_PER_FRAME = 1000


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Initialize pygame
pygame.init()
pygame.font.init()

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulated Annealing TSP")
clock = pygame.time.Clock()

# Generate random nodes
nodes = Node.random_nodes(30, WIDTH - 50, HEIGHT - 50)

# Set up the TSP problem
tsp = TSP(nodes)

# Create font for displaying the distance
font = pygame.font.SysFont('Arial', FONT_SIZE)

# Main loop
iter_count = 0
while True:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Run simulated annealing algorithm for fixed number of iterations
    for _ in range(ITER_PER_FRAME):
        result = tsp.anneal()
        iter_count += 1

        # If the algorithm has converged, break out of the loop
        if result is not None:
            break

    # Clear the screen
    screen.fill(WHITE)

    # Draw the nodes
    for node in nodes:
        pygame.draw.circle(screen, BLACK, (int(node.x), int(node.y)), NODE_RADIUS)

    # Draw the edges
    order, distance = tsp.get_best()
    for i in range(tsp.num_nodes - 1):
        node1 = nodes[order[i]]
        node2 = nodes[order[i + 1]]
        pygame.draw.line(screen, BLUE, (int(node1.x), int(node1.y)), (int(node2.x), int(node2.y)), LINE_WIDTH)

    # Draw the last edge
    node1 = nodes[order[-1]]
    node2 = nodes[order[0]]
    pygame.draw.line(screen, BLUE, (int(node1.x), int(node1.y)), (int(node2.x), int(node2.y)), LINE_WIDTH)

    # Draw the distance
    text = font.render(f"Distance: {distance:.2f}", True, BLACK)
    screen.blit(text, (10, 10))

    # Draw the iteration count
    text = font.render(f"Iterations: {iter_count}", True, BLACK)
    screen.blit(text, (10, 50))


    # Update the screen
    pygame.display.update()

    # Cap the frame rate
    clock.tick(FPS)
