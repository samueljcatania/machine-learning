import matplotlib.pyplot as plt
from helpers import box, circle


def create_data(fig: plt) -> list:
    # Set axis limits and behaviour
    ax = fig.add_subplot(2, 3, 6)
    ax.set_xlim(-80, 80)
    ax.set_ylim(-80, 80)
    ax.axis("equal")
    ax.title.set_text("Figure 6")

    # List to hold all points and their colours
    data = []

    # Green circle
    x_list, y_list = circle.generate(70, 80, 1)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="lime", s=20).get_offsets()):
        data.append([element.tolist(), "green"])

    # Black box
    x_list, y_list = box.generate(150, -10, 10, 50, 70, 1, 1, 1, False)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="black", s=20).get_offsets()):
        data.append([element.tolist(), "black"])

    # Red box
    x_list, y_list = box.generate(150, -10, 10, -60, -40, 1, 1, 1, False)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="red", s=20).get_offsets()):
        data.append([element.tolist(), "red"])

    return data
