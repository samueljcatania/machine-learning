import math
import random
import numpy as np


def k_means(data: list, k: int):
    # Randomly shuffle the list of data
    np.random.shuffle(data)

    # Randomly choose k cluster centers and remove class (as cluster centers don't have classes)
    cluster_centers = [point[0] for point in random.choices(data, k=k)]

    # Boolean variable to track if any of the cluster centers changed
    changed = True

    # List to hold final linked data
    final_linked_data = []

    while changed:
        # List to hold the distances from each point to each cluster center
        distances = []

        # List to hold the data points linked to each cluster center
        clustered_data = []

        for k_value in range(0, k):
            clustered_data.append([])

        # Calculate the distance between all the data points and each cluster center
        for point in data:

            # List that temporarily holds all the distances between a point and a cluster center, as well as the
            # original coordinates and class of that point
            temp_list = []

            # Calculate the euclidian distance for each point to the given cluster center and append it to a list
            for center in cluster_centers:
                euclidian_distance = math.sqrt(
                    ((point[0][0] - center[0]) ** 2) + ((point[0][1] - center[1]) ** 2))

                temp_list.append(euclidian_distance)

            distances.append([temp_list, point])

        # Assign data points to the nearest cluster center by the distance that was just calculated
        for point in distances:
            # Get the index of the smallest distance to a cluster center and use that as the index of clustered_data to
            # append to (so each index in clustered_data will hold a list of data points that are closest to that
            # cluster, the cluster's number being represented by index)
            clustered_data[point[0].index(min(point[0]))].append(point[1])

        # List that holds the coordinates of the new cluster centers
        new_cluster_centers = []

        # Recalculate the cluster centers with the data points linked to each cluster center
        for center in clustered_data:

            mean_x = 0
            mean_y = 0

            for point in center:
                mean_x += point[0][0]
                mean_y += point[0][1]

            mean_x = mean_x / (len(center) if len(center) > 0 else 1)
            mean_y = mean_y / (len(center) if len(center) > 0 else 1)

            new_cluster_centers.append([mean_x, mean_y])

        # Create a variable to change the changed variable
        temp_changed = False

        for k_value in range(0, k):
            if new_cluster_centers[k_value] != cluster_centers[k_value]:
                temp_changed = True

        changed = temp_changed

        if changed:

            cluster_centers = new_cluster_centers
        else:
            final_linked_data = clustered_data

    return cluster_centers, final_linked_data
