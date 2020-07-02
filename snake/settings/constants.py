import numpy as np

SIZE = (32, 32) # size of the grid world
SNAKE_SIZE = 3 # initial size of the snake
# numeric representation for different types of objects
WALL = 255
FOOD_BLOCK = 64
SNAKE_BLOCK = 100
"""
DIRECTIONS:
    0: UP
    1: RIGHT
    2: DOWN
    3: LEFT
"""
DIRECTIONS = [np.array([-1, 0]),
              np.array([0, 1]),
              np.array([1, 0]),
              np.array([0, -1])]
# rewards for different events
DEAD_REWARD = -1.0
MOVE_REWARD = 0.0
EAT_REWARD = 1.0