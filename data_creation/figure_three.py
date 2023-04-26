import matplotlib.pyplot as plt
from helpers import box, parabola


def create_data(fig: plt) -> list:
    # Set axis limits and behaviour
    ax = fig.add_subplot(2, 3, 3)
    ax.set_xlim(-80, 80)
    ax.set_ylim(-80, 80)
    ax.axis("equal")
    ax.title.set_text("Figure 3")

    # List to hold all points and their colours
    data = []

    # Green box
    x_list, y_list = box.generate(175, -35, -10, 10, 45, 1, 1, 1, False)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="lime", s=20).get_offsets()):
        data.append([element.tolist(), "green"])

    # Red box
    x_list, y_list = box.generate(175, 16, 40, 11, 44, 1, 1, 1, False)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="red", s=20).get_offsets()):
        data.append([element.tolist(), "red"])

    # Black dots
    x_list, y_list = parabola.generate(-70, 70, -70, 30, 5, 5, 0.8, True)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="black", s=20).get_offsets()):
        data.append([element.tolist(), "black"])

    return data
