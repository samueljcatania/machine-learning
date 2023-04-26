import numpy as np
import heapq
import math


# k-NN algorithm runs through many possible k values to find the most accurate k value
def knn_algorithm(figure_data: list) -> tuple[list[float], list[float], int, int]:
    # List that stores the accuracies of each k value during cross validation
    cv_k_accuracies = []

    # Stores all the test accuracies of the k values on unseen test data
    k_test_accuracies = []

    # Stores the overall accuracy of tuned k value on test data
    test_accuracy = 0

    # Define the number of k-folds for cross validation
    k_folds = 10

    # Define the maximum k value in the k-NN algorithm to test for
    max_k = 50

    # Randomly shuffle the list of data
    np.random.shuffle(figure_data)

    # Split the data into training and testing data
    data_split = [sub_element.tolist() for sub_element in
                  [element for element in np.array_split(np.array(figure_data, dtype=object), 100)]]

    # Define the training data as 20% of the data and flatten the list
    training_data = [item for sublist in data_split[:20] for item in sublist]

    # Separate the training data into k-folds
    training_data = [sub_element.tolist() for sub_element in
                     [element for element in np.array_split(np.array(training_data, dtype=object), k_folds)]]

    # Define the testing data as 80% of the data
    testing_data = data_split[20:]

    # Flatten list
    testing_data = [item for sublist in testing_data for item in sublist]

    for k in range(1, max_k):
        # Stores the overall accuracy of all cross-validations of the given k value
        cv_accuracy = 0

        # Stores the number of successful class predictions to calculate accuracy of the given k value on test data
        successful_predictions = 0

        # Cross-validate the (k-2) folds to get the average accuracy of the k value for the training data
        for k_fold in range(0, k_folds):
            # Stores the number of successful class predictions to later calculate accuracy of the given
            # cross-validation
            cross_validation_successes = 0

            # Define the validation set
            validation_set = training_data[k_fold]

            # Define the rest of the training data that doesn't include the validation set
            cv_training_data = training_data[:]
            cv_training_data.remove(validation_set)

            # Loop through each data point in the testing fold
            for data_point in validation_set:
                class_weights = predict_classification(get_k_closest_points(k, data_point, cv_training_data))

                # With each successful prediction, increment the cross_validation_successes by 1
                if max(class_weights, key=lambda x: x[1])[0] == data_point[1]:
                    cross_validation_successes += 1

            # Add the success rate of predictions as a percentage to the total accuracy
            cv_accuracy += (cross_validation_successes / len(validation_set) * 100)

        # Find the average accuracy of all cross-validations
        cv_k_accuracies.append(cv_accuracy / k_folds)

    # Find the k value with the lowest error rate
    tuned_k_value = cv_k_accuracies.index(max(cv_k_accuracies)) + 1

    for k in range(1, max_k):
        # Stores the number of successful class predictions to calculate accuracy of the given k value on test data
        successful_predictions = 0

        # Calculate the test accuracy for all the k values on unseen test data
        for data_point in testing_data:
            class_weights = predict_classification(get_k_closest_points(k, data_point, training_data))

            # With each successful prediction, increment the successful_predictions by 1
            if max(class_weights, key=lambda x: x[1])[0] == data_point[1]:
                successful_predictions += 1

        # If this k is the hyper-tuned k, get the accuracy
        if k == tuned_k_value:
            test_accuracy = (successful_predictions / len(testing_data) * 100)

        # Add the success rate of predictions as a percentage to the total accuracy
        k_test_accuracies.append(successful_predictions / len(testing_data) * 100)

    return cv_k_accuracies, k_test_accuracies, tuned_k_value, test_accuracy


# Returns the k closest neighbours to a give point
def get_k_closest_points(k: int, focus_point: np, f_data: list) -> list:
    # List to store the calculated euclidian distances of all points to the given focus point
    distances = []

    # Calculate the euclidian distance for each point to the given focus point and append it to the list
    for fold in f_data:
        for point in fold:
            euclidian_distance = math.sqrt(
                ((point[0][0] - focus_point[0][0]) ** 2) + ((point[0][1] - focus_point[0][1]) ** 2))

            # If the distance between the focus point and a neighbouring point is 0, discard that point and don't use it
            if euclidian_distance != 0:
                distances.append([point[1], euclidian_distance])

    # Return a list with the k-smallest distances (set the key to the heapq.smallest() function as the 1 index of each
    # element in the list distances, as index 1 contains the distance value
    return heapq.nsmallest(k, distances, key=lambda x: x[1])


# Predicts the class of a given point
def predict_classification(k_neighbours: list) -> list:
    # List to store the weighted classes of the k neighbours
    class_weights = [["black", 0], ["red", 0], ["green", 0], ["pink", 0], ["yellow", 0]]

    # Loop through all k neighbours
    for neighbour in k_neighbours:

        # Loop through all the current class weights in class_weights
        for class_w in class_weights:

            # If the class already exists in class_weights, add the weight to it
            if class_w[0] == neighbour[0]:
                # The distance weight is simply the inverse of the distance
                class_w[1] += 1 / neighbour[1]

    return class_weights
