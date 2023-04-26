from numpy import random


def generate(number_of_dots: int, x_min: float, x_max: float, y_min: float,
             y_max: float, x_randomness: float, y_randomness: float, random_chance: float,
             negative_random: bool):
    # Lists to store points
    x_list = []
    y_list = []

    # Compute the x and y value for each point
    for i in range(0, number_of_dots):

        # Random chance outlines the percentage chance a given point will be subject to randomness
        if random.rand() < random_chance:

            # 50 percent chance the point is shifted randomly in a negative direction
            if negative_random and random.rand() < 0.5:
                x_list.append(random.randint(x_min, x_max) - (random.rand() * ((x_max - x_min) * x_randomness / 10)))
                y_list.append(random.randint(y_min, y_max) - (random.rand() * ((y_max - y_min) * y_randomness / 10)))

            # 50 percent chance the point is shifted randomly in a positive direction
            else:
                x_list.append(random.randint(x_min, x_max) + (random.rand() * ((x_max - x_min) * x_randomness / 10)))
                y_list.append(random.randint(y_min, y_max) + (random.rand() * ((y_max - y_min) * y_randomness / 10)))

        else:
            x_list.append(random.randint(x_min, x_max))
            y_list.append(random.randint(y_min, y_max))

    return x_list, y_list
