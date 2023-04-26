import matplotlib.pyplot as plt
from helpers import box


def create_data(fig: plt) -> list:
    # Set axis limits and behaviour
    ax = fig.add_subplot(2, 3, 2)
    ax.set_xlim(-80, 80)
    ax.set_ylim(-80, 80)
    ax.axis("equal")
    ax.title.set_text("Figure 2")

    # List to hold all points and their colours
    data = []

    # Black dots
    x_list, y_list = box.generate(150, -70, 70, -70, 70, 1, 1, 1, False)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="black", s=20).get_offsets()):
        data.append([element.tolist(), "black"])

    # Red box
    x_list, y_list = box.generate(150, 22, 27, 20, 25, 5, 5, 1, False)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="red", s=20).get_offsets()):
        data.append([element.tolist(), "red"])

    # Green box
    x_list, y_list = box.generate(150, 10, 15, -18, -13, 5, 5, 1, False)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="lime", s=20).get_offsets()):
        data.append([element.tolist(), "green"])

    return data
