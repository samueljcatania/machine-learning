# Run this file to apply the k-Means and the Agglomerative clustering algorithms on the 6 data sets in which the data
# have no labels or cluster indicators to begin with to discover what clusters will be produced.

from data_creation import figure_one, figure_two, figure_three, figure_four, figure_five, figure_six
from clustering_algorithms import k_means, agglomerative
import matplotlib.pyplot as plt


# Helper function to plot the k-Means clusters
def plot_k_subplots(centers_list: list, linked_points_list: list):
    k_fig, axs = plt.subplots(2, 3, figsize=(20, 7))

    # List of colors
    colors = ["red", "blue", "lime", "orange", "purple"]

    # Make fullscreen
    k_manager = plt.get_current_fig_manager()
    k_manager.resize(*k_manager.window.maxsize())

    # Set the title of the entire plot window
    k_fig.suptitle(
        "Each color represents a cluster in k-Means (The big dots represent the cluster center (or cluster mean) of "
        "that color cluster)",
        fontsize=24)

    # Variables for controlling subplot positioning
    column = 0
    row = 0

    # Set axis limits and behaviour
    for index, k_means_figure in enumerate(linked_points_list):

        for k, cluster in enumerate(k_means_figure):

            x_values = []
            y_values = []

            for point in cluster:
                x_values.append(point[0][0])
                y_values.append(point[0][1])

            axs[row, column].scatter(x_values, y_values, c=colors[k])
            axs[row, column].scatter(centers_list[index][k][0], centers_list[index][k][1], c=colors[k], s=200,
                                     edgecolors='black')

        axs[row, column].set_title("k-Means Clusters - Figure " + str(index + 1))
        axs[row, column].axis("equal")

        # If at the end of the row, go one row down
        if column < 2:
            column += 1
        else:
            column = 0
            row += 1

    plt.show()


if __name__ == '__main__':
    # List that stores the cluster centers of the figures
    cluster_center_list = []

    # List that stores the cluster linked points of the figures
    cluster_linked_point_list = []

    # Program start message
    print("Program started.\n")

    fig = plt.figure(figsize=(15, 10))

    # Make fullscreen
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())

    # Set the title of the entire plot window
    fig.suptitle("The Data Generated and Plotted for Figures 1-6", fontsize=24)

    # Generating data message
    print("Generating data...", end="")

    # Add the data of each figure to a list
    data = [figure_one.create_data(fig), figure_two.create_data(fig), figure_three.create_data(fig),
            figure_four.create_data(fig), figure_five.create_data(fig), figure_six.create_data(fig)]

    print("done\n")

    # Showing data message
    print("Plotting and showing generated data...", end="")
    plt.show(block=False)
    print("done\n")

    # Loop through each figure to apply the k-Means algorithm
    for figure_number, figure in enumerate(data):
        # Variables for controlling subplot positioning
        c = 0
        r = 0

        # Running k-NN algorithm message
        print("Running the k-Means algorithm on Figure " + str(figure_number + 1) + "...", end="")

        # Number of clusters in k-Means
        k_clusters = 0

        if figure_number == 0:
            k_clusters = 3
        elif figure_number == 1:
            k_clusters = 3
        elif figure_number == 2:
            k_clusters = 3
        elif figure_number == 3:
            k_clusters = 5
        elif figure_number == 4:
            k_clusters = 4
        elif figure_number == 5:
            k_clusters = 3

        cluster_centers, cluster_linked_points = k_means.k_means(figure, k_clusters)

        cluster_center_list.append(cluster_centers)
        cluster_linked_point_list.append(cluster_linked_points)

        print("done\n")

        # Showing data message
        print("Plotting and showing agglomerative clustering data...", end="")
        agglomerative.agglomerative_clustering(figure, figure_number)
        print("done\n")

        # If at the end of the row, go one row down
        if c < 2:
            c += 1
        else:
            c = 0
            r += 1

    print("\nPlotting and showing k-Means cluster data...", end="")
    plot_k_subplots(cluster_center_list, cluster_linked_point_list)
    print("done\n")
