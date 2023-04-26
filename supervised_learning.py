# Run this file to apply the k-NN algorithm on the 6 data sets, using cross-validation to find the best k for each
# problem (that is the k that produces the smallest predictive accuracy on the validation set) to discover the test
# accuracy for each of the 6 data sets (which would hypothetically be the most reliable estimate of the predictive
# accuracy for the future unseen test data). The data will be randomly generated and sampled to form the training set,
# validation set, and test set.

from data_creation import figure_one, figure_two, figure_three, figure_four, figure_five, figure_six
from supervised_learning_algorithms import k_NN_algorithm
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
        axs[row, column].set_title("k Accuracy  - Figure " + str(index + 1))

        # If at the end of the row, go one row down
        if column < 2:
            column += 1
        else:
            column = 0
            row += 1

    plt.show()


if __name__ == '__main__':
    # Program start message
    print("Program started.\n")

    # Stores a list of all the cross-validation accuracies for each figure
    all_cv_accuracies = []

    # Stores a list of all the test accuracies for each figure
    all_test_accuracies = []

    # Stores a list of the chosen tuned hyperparameters
    tuned_k_values = []

    # Stores the test data accuracy of each of the tuned hyperparameter
    test_accuracies = []

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

    # Loop through each figure to apply the k-NN algorithm
    for figure_number, figure in enumerate(data):
        # Running k-NN algorithm message
        print("Running the k-NN algorithm on Figure " + str(figure_number + 1) + "...", end="")
        cv_k_a, td_k_a, tuned_k, test_acc = k_NN_algorithm.knn_algorithm(figure)

        all_cv_accuracies.append(cv_k_a)
        all_test_accuracies.append(td_k_a)
        tuned_k_values.append(tuned_k)
        test_accuracies.append(test_acc)

        print("done\n")

    # Showing data message
    print("Plotting and showing generated data...", end="")
    plt.show(block=False)
    print("done\n")

    for i in range(0, 6):
        print("The best k for figure " + str(i + 1) + " is k=" + str(
            tuned_k_values[i]) + " with a test accuracy on future unseen test data of " + str(test_accuracies[i]))

    # Showing k findings message
    print("\nPlotting and showing k value data...", end="")
    plot_k_subplots(all_cv_accuracies, all_test_accuracies)
    print("done\n")
