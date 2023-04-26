import numpy as np
from numpy import random


def generate(number_of_dots: int, radius: float, randomness: float):
    # Calculate 'angles' to plot the dots on around a circle
    angles = np.linspace(0, 2 * np.pi, number_of_dots)

    # Lists to store points
    x_list = []
    y_list = []

    # Compute the x and y value for each point
    for angle in angles:
        x_list.append(radius * np.cos(angle) + (random.rand() * (radius * randomness / 10)))
        y_list.append(radius * np.sin(angle) + (random.rand() * (radius * randomness / 10)))

    return x_list, y_list
