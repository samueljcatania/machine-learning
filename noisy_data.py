# Run this file to apply the decision tree and k-NN algorithms on the 6 data sets when the data sets are injected with
# noisy data (set to 20% of all the data) to discover if overfitting happens. (Overfitting is a
# phenomenon where the model is trained to have very small (0%) training error but the test error actually
# increases).  Try to use the validation set (which also contains “noise”) to choose the best hyper-parameters (such
# as pruning levels for decision trees, k for k-NN).  Report the test accuracy for such models as the most reliable
# estimate of the predictive accuracy of your model for the future unseen test data.

from data_creation import figure_one, figure_two
from helpers import noise
from supervised_learning_algorithms import k_NN_algorithm, decision_tree
import matplotlib.pyplot as plt


# Helper function to plot the k values with their accuracies
def plot_k_subplots(cv_k_data: list, test_k_data: list):
    k_fig, axs = plt.subplots(2, 3, figsize=(20, 7))

    # Make fullscreen
    k_manager = plt.get_current_fig_manager()
    k_manager.resize(*k_manager.window.maxsize())

    # Set the title of the entire plot window
    k_fig.suptitle(
        "Blue Line = Test Accuracy on Cross-Validation with 10 folds, Red = Test Accuracy on Unseen Test Data",
        fontsize=24)

    # Variables for controlling subplot positioning
    column = 0
    row = 0

    # Set axis limits and behaviour
    for index, k_figure in enumerate(cv_k_data):
        axs[row, column].plot(range(len(k_figure)), k_figure, 'tab:blue')
        axs[row, column].plot(range(len(test_k_data[index])), test_k_data[index], 'tab:red')
        axs[row, column].set_title("k Accuracy - Figure " + str(index + 1))

        # If at the end of the row, go one row down
        if column < 2:
            column += 1
        else:
            column = 0
            row += 1

    plt.show()


# Adds noise to the data
def noise_creation(data_list: list, percentage_of_noise: float):
    number_of_points = (int((len(data_list) * percentage_of_noise) / 3))

    noise_data = []

    # Black dot noise
    x_list, y_list = noise.generate(number_of_points, -20, 20, -60, 60)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="purple", s=20).get_offsets()):
        noise_data.append([element.tolist(), "purple"])

    # Green dot noise
    x_list, y_list = noise.generate(number_of_points, -20, 20, -60, 60)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="yellow", s=20).get_offsets()):
        noise_data.append([element.tolist(), "yellow"])

    # Red dot noise
    x_list, y_list = noise.generate(number_of_points, -20, 20, -60, 60)

    # Add the points with the respective colour to the main list of points
    for element in (plt.scatter(x_list, y_list, c="orange", s=20).get_offsets()):
        noise_data.append([element.tolist(), "orange"])

    data_list = data_list + noise_data

    return data_list


if __name__ == '__main__':
    # Program start message
    print("Program started.\n")

    # Stores a list of all the cross-validation accuracies for each figure for knn
    all_cv_knn_accuracies = []

    # Stores a list of all the test accuracies for each figure for knn
    all_test_knn_accuracies = []

    # Stores a list of the chosen tuned hyperparameters in knn
    tuned_k_values = []

    # Stores the test data accuracy of each of the tuned hyperparameters in knn
    knn_test_accuracies = []

    # Stores the test data accuracy of each decision tree
    all_dtree_test_accuracies = []

    # Stores a list of the chosen tuned hyperparameters in knn
    tuned_dtree_hyperparameters = []

    fig = plt.figure(figsize=(15, 10))

    # Make fullscreen
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())

    # Set the title of the entire plot window
    fig.suptitle("The Data Generated and Plotted for Figures 1 and 2", fontsize=24)

    # The percentage of noise to be added
    percntge_of_noise = 0.20
    print("The current percentage of noise is set to: " + str(percntge_of_noise * 100) + "%")

    # Generating data message
    print("Generating data and adding noise...", end="")

    # Add the data of each figure to a list
    data = [noise_creation(figure_one.create_data(fig), percntge_of_noise),
            noise_creation(figure_two.create_data(fig), percntge_of_noise)]

    print("done\n")

    # Loop through each figure to apply the k-NN algorithm and decision tree algorithm
    for figure_number, figure in enumerate(data):
        # Running k-NN algorithm message
        print("Running the k-NN algorithm on Figure " + str(figure_number + 1) + "...", end="")
        cv_k_a, td_k_a, tuned_k, test_acc = k_NN_algorithm.knn_algorithm(figure)

        print("done\n")

        all_cv_knn_accuracies.append(cv_k_a)
        all_test_knn_accuracies.append(td_k_a)
        tuned_k_values.append(tuned_k)
        knn_test_accuracies.append(test_acc)

        print("Running the decision tree algorithm on Figure " + str(figure_number + 1) + "...", end="")
        dtree_accuracy, dtree_hyperparameters = decision_tree.decision_tree(figure)

        all_dtree_test_accuracies.append(dtree_accuracy)
        tuned_dtree_hyperparameters.append(dtree_hyperparameters)

        print("done\n")

        # Showing data message
        print("Plotting and showing generated data...", end="")
        plt.show(block=False)
        print("done\n")

    for i in range(0, 2):
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

    # Showing k findings message
    print("\nPlotting and showing k value data...", end="")
    plot_k_subplots(all_cv_knn_accuracies, all_test_knn_accuracies)
    print("done\n")
