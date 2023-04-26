import matplotlib.pyplot as plt
from helpers import box


def create_data(fig: plt) -> list:
    # Set axis limits and behaviour
    ax = fig.add_subplot(2, 3, 5)
    ax.set_xlim(-80, 80)
    ax.set_ylim(-80, 80)
    ax.axis("equal")
    ax.title.set_text("Figure 5")

    # List to hold all points and their colours
    data = []

    # Green line
    x_list, y_list = box.generate(200, -70, 65, 38, 40, 0, 20, 0.5, True)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="lime", s=20).get_offsets()):
        data.append([element.tolist(), "green"])

    # Black line
    x_list, y_list = box.generate(150, -35, 10, 5, 7, 1, 20, 0.5, True)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="black", s=20).get_offsets()):
        data.append([element.tolist(), "black"])

    # Red line
    x_list, y_list = box.generate(250, -63, 67, -27, -25, 1, 20, 0.6, True)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="red", s=20).get_offsets()):
        data.append([element.tolist(), "red"])

    # Pink line
    x_list, y_list = box.generate(150, -25, 10, -56, -54, 1, 20, 0.5, True)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="fuchsia", s=20).get_offsets()):
        data.append([element.tolist(), "pink"])

    return data
