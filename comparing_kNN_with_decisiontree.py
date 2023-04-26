# Run this file to apply the k-NN and decision tree algorithms on the 6 data sets, comparing the results of both
# algorithms to discover which one performs better on each of the 6 data sets.

from data_creation import figure_one, figure_two, figure_three, figure_four, figure_five, figure_six
from supervised_learning_algorithms import k_NN_algorithm, decision_tree
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Program start message
    print("Program started.\n")

    # Stores a list of the chosen tuned hyperparameters in knn
    tuned_k_values = []

    # Stores the test data accuracy of each of the tuned hyperparameters in knn
    knn_test_accuracies = []

    # Stores the test data accuracy of each decision tree
    all_dtree_test_accuracies = []

    # Stores a list of the chosen tuned hyperparameters in knn
    tuned_dtree_hyperparameters = []

    fig = plt.figure()

    # Generating data message
    print("Generating data...", end="")

    # Add the data of each figure to a list
    data = [figure_one.create_data(fig), figure_two.create_data(fig), figure_three.create_data(fig),
            figure_four.create_data(fig), figure_five.create_data(fig), figure_six.create_data(fig)]

    print("done\n")

    # Loop through each figure to apply the k-NN algorithm and decision tree algorithm
    for figure_number, figure in enumerate(data):
        # Running k-NN algorithm message
        print("Running the k-NN algorithm on Figure " + str(figure_number + 1) + "...", end="")
        cv_k_a, td_k_a, tuned_k, test_acc = k_NN_algorithm.knn_algorithm(figure)

        print("done\n")

        tuned_k_values.append(tuned_k)
        knn_test_accuracies.append(test_acc)

        print("Running the decision tree algorithm on Figure " + str(figure_number + 1) + "...", end="")
        dtree_accuracy, dtree_hyperparameters = decision_tree.decision_tree(figure)

        all_dtree_test_accuracies.append(dtree_accuracy)
        tuned_dtree_hyperparameters.append(dtree_hyperparameters)

        print("done\n")

    for i in range(0, 6):
        print("Figure " + str(i + 1) + ":")
        print("\tTrained hyperparameters for Figure " + str(i + 1) + " k-NN algorithm are:")
        print("\t\tk=" + str(tuned_k_values[i]))
        print("\t\t" + str(
            knn_test_accuracies[i]) + " -> k-NN test accuracy on future unseen test data with tuned hyperparameters")
        print("\tTrained hyperparameters for Figure " + str(i + 1) + " Decision Tree algorithm are:")
        print("\t\tk=" + str(tuned_dtree_hyperparameters[i]))
        print("\t\t" + str(all_dtree_test_accuracies[
                               i]) + " -> Decision Tree test accuracy on future unseen test data with tuned "
                                     "hyperparameters")

        if all_dtree_test_accuracies[i] > knn_test_accuracies[i]:
            print("\n\tFor Figure " + str(i + 1) + " the Decision Tree model performs better.\n")
        elif all_dtree_test_accuracies[i] < knn_test_accuracies[i]:
            print("\n\tFor Figure " + str(i + 1) + " the k-NN model performs better.\n")
        else:
            print("\n\tFor Figure " + str(i + 1) + " the both models perform the same.\n")
