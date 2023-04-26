from numpy import random


def generate(x_min: int, x_max: int, y_min: int,
             y_max: int, x_randomness: float, y_randomness: float, random_chance: float,
             negative_random: bool):
    # Lists to store points
    x_list = []
    y_list = []

    # Compute the x and y value for each point
    for i in range(x_min, x_max + 1):

        y_value = ((i * i) / 50) - 60

        if y_min <= y_value <= y_max:

            # Random chance outlines the percentage chance a given point will be subject to randomness
            if random.rand() < random_chance:

                chance = random.rand()

                # 25 percent chance the point is shifted randomly in a negative direction on both axes
                if negative_random and chance < 0.25:
                    x_list.append(i - (random.rand() * x_randomness))
                    y_list.append(y_value - (random.rand() * y_randomness))

                # 25 percent chance the point is shifted randomly in a positive direction on the x-axis and
                # negative direction on the y-axis
                elif negative_random and 0.25 <= chance < 0.5:
                    x_list.append(i + (random.rand() * x_randomness))
                    y_list.append(y_value - (random.rand() * y_randomness))

                # 25 percent chance the point is shifted randomly in a negative direction on the x-axis and
                # positive direction on the y-axis
                elif negative_random and 0.5 <= chance < 0.75:
                    x_list.append(i - (random.rand() * x_randomness))
                    y_list.append(y_value + (random.rand() * y_randomness))

                # 25 percent chance the point is shifted randomly in a positive direction on both axes
                else:
                    x_list.append(i + (random.rand() * x_randomness))
                    y_list.append(y_value + (random.rand() * y_randomness))

            else:
                x_list.append(i)
                y_list.append(y_value)

    return x_list, y_list
