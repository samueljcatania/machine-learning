from numpy import random


def generate(max_dots: int, x_min: int, x_max: int, y_min: int, y_max: int,):
    # Lists to store points
    x_list = []
    y_list = []

    # Compute the x and y value for each point
    for _ in range(0, max_dots):
        x_list.append(random.randint(x_min, x_max))
        y_list.append(random.randint(y_min, y_max))

    return x_list, y_list
