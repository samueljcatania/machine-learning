import matplotlib.pyplot as plt
from helpers import box


def create_data(fig: plt) -> list:
    # Set axis limits and behaviour
    ax = fig.add_subplot(2, 3, 4)
    ax.set_xlim(-80, 80)
    ax.set_ylim(-80, 80)
    ax.axis("equal")
    ax.title.set_text("Figure 4")

    # List to hold all points and their colours
    data = []

    # Red dots
    x_list, y_list = box.generate(150, -70, 70, -60, 60, 1, 1, 1, False)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="red", s=20).get_offsets()):
        data.append([element.tolist(), "red"])

    # Green box
    x_list, y_list = box.generate(150, 23, 30, 18, 25, 3, 3, 1, False)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="lime", s=20).get_offsets()):
        data.append([element.tolist(), "green"])

    # Black box
    x_list, y_list = box.generate(150, 23, 30, -10, -3, 3, 3, 1, False)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="black", s=20).get_offsets()):
        data.append([element.tolist(), "black"])

    # Pink box
    x_list, y_list = box.generate(150, -25, -18, 15, 22, 3, 3, 1, False)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="fuchsia", s=20).get_offsets()):
        data.append([element.tolist(), "pink"])

    # Yellow box
    x_list, y_list = box.generate(150, -20, -13, -25, -18, 3, 3, 1, False)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="yellow", s=20).get_offsets()):
        data.append([element.tolist(), "yellow"])

    return data
