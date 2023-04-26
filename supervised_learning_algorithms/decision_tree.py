from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier


# Decision tree attempts to classify given data
def decision_tree(figure_data: list):
    # Split dataset into training set (20%) and test set (80%)
    x_train, x_test, y_train, y_test = train_test_split([coords[0] for coords in figure_data],
                                                        [coords[1] for coords in figure_data], test_size=0.8,
                                                        random_state=100)  # 80% training and 20% test

    # Create a dictionary of parameters to use in GridSearchCV
    params = {
        "criterion": ["gini", "entropy"],
        "splitter": ["best", "random"],
        "max_depth": [None, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],
        "max_features": [None, 'sqrt', 'log2', 0.2, 0.4, 0.6, 0.8],

    }

    # Use GridSearchCV to tune the hyperparameters and apply cross-validation at the same time.
    clf = GridSearchCV(
        estimator=DecisionTreeClassifier(),
        param_grid=params,
        cv=10,
        n_jobs=5,
        verbose=1,
    )

    # Turn console output off
    clf.verbose = False

    # Train the Decision Tree with the training data
    clf.fit(x_train, y_train)

    # Now get the mode of the Decision Tree with the best trained hyperparameters to use
    best_model = clf.best_estimator_

    # Return the accuracy of the best hyperparameter-trained Decision Tree model on the test data
    return best_model.score(x_test, y_test) * 100, clf.best_params_


