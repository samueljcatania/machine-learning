# machine-learning

### Description
Supervised K-NN classification and unsupervised K-Means clustering machine learning algorithms 
built from scratch in Python using NumPy and Matplotlib, in addition to modified Decision Tree
and Agglomerative Clustering machine learning algorithms implemented with the help of scikit-learn. 

### Focus
The machine learning algorithms were run on 6 separate data sets, displayed with the help of Matplotlib. The dendrograms were built using SciPy and Pandas.

<img src='https://user-images.githubusercontent.com/69449284/234444832-60127910-4eb9-42f1-b3c7-0f8915b2e430.png' width='800'>

There are 4 .py files with main functions, (**supervised_learning.py**, **clustering.py**, **comparing_KNN_with_decisiontree.py**, and **noisy_data.py**).

Each main .py file is a driver file responsible for running and testing the different functions of the implemented machine learning algorithms in different scenarios.


## supervised_learning.py

Here, the 6 data sets are each individually run on the supervised k-nearest neighbors algorithm. Within the 6 data sets, 
each different color indicates a different class, treated as ground truth. The data is sampled to form the training set, 
validation set, and test set, in which the validation and test sets are set to be large to get reliable estimates of predictive 
accuracy. Cross-validation is used tune the hyperparameter k for each set of data (the best k would hypothetically produce the 
smallest possible predictive accuracy on the validation set). The test accuracies that are reported would thus be the most reliable 
estimate of the predictive accuracy for my k-NN algorithm for future unseen test data.

<img src='https://user-images.githubusercontent.com/69449284/234446719-6a9419f7-a175-41de-871f-4ab40c3872e4.png' width='800'>


## clustering.py

Here, the 6 data sets are each individually run on the unsupervised k-Means and Agglomerative Clustering algorithms. 
Within the 6 data sets, no colors are assigned initially to indicate different classes or labels as 
ground truth. Instead, each data set will start with no classes or cluster indicators, and the clustering algorithms will 
attempt to cluster the data set. The clustering algorithms themselves will colour the clusters according to their best 
attempt at discovering clusters within the data. The k-Means and Agglomerative Clustering algorithms will simply colour in 
the original data points provided, with the Agglomerative Clustering algorithm additionally producing a Dendrogram with coloured 
heirarchies, each representing a separate cluster of data.

<img src='https://user-images.githubusercontent.com/69449284/234446691-ae9b44dd-d357-4aad-85c3-1d98ae87d49f.png' width='800'>
<img src='https://user-images.githubusercontent.com/69449284/234446694-76b5bd0f-adce-4f93-a14e-e8e4c6ce6197.png' width='400'>
<img src='https://user-images.githubusercontent.com/69449284/234452296-885beaca-2c4b-4bf6-b310-e906f12ee0d6.png' width='400'>


## comparing_KNN_with_decisiontree.py

A machine learning algorithm is usually called “better”, if with the training data of the same size, algorithm X 
predicts more accurately than algorithm Y, on the test data. Here, accuracies from a decision tree algorithm implemented 
using scikit-learn are compared with the accuracies from the k-nearest neighbors algorithm, when each algorithm is run on the 
6 data sets, to see which algorithm performs better for each.

The followng is a portion of output from running this file. Despite the complexity of my implementation of the k-NN algorithm, 
this portion of output is a prime example of one of the challenges faced when designing and implementing machine learning algorithms.
Here, overfitting occurs from the k-NN algorithm, in which the model has trained its hyperparameters to fit exactly against the 
training data it was given (hence k=1). When this happens, the algorithm cannot perform accurately against new unseen data.

```
Figure 2:
  Trained hyperparameters for Figure 2 k-NN algorithm are:
    k=1
    95.42857142857143 -> k-NN test accuracy on future unseen test data with tuned hyperparameters
    
  Trained hyperparameters for Figure 2 Decision Tree algorithm are:
    k={'criterion': 'gini', 'max_depth': None, 'max_features': None, 'splitter': 'best'}
    95.55555555555556 -> Decision Tree test accuracy on future unseen test data with tuned hyperparameters
```

## noisy_data.py

The behavior of supervised learning algorithms can be heavily affected when the data provided contains noisy/outlier/anomaly data.
Within the data sets, each different color indicates a different class, treated as ground truth. But in addition to the original data,
noisy data is additionally generated and placed amongst the original data with a probability of 20%. This new set of noisy data mixed 
in with the original data is then sampled to form the training set, validation set, and test set, in which  Here, a decision tree algorithm 
implemented using scikit-learn and the k-nearest neighbors algorithm are run on data sets injected with noisy data. The test accuracies of both
algorithms are then compared, and the test accuracies of the k-NN algorithm are additionally graphed.

<img src='https://user-images.githubusercontent.com/69449284/234446704-0fb9dde6-22c1-4444-8690-675bef843951.png' width='800'>
<img src='https://user-images.githubusercontent.com/69449284/234454890-6b951d5a-755f-4671-a2db-9f80fd4e7ea1.png' width='800'>

Additionally, the followng is a portion of output from running this file. Along with the findings from the charts, overfitting is clearly occuring.
```
Figure 1:
  Trained hyperparameters for Figure 1 k-NN algorithm are:
    k=1
    73.98945518453426 -> k-NN test accuracy on future unseen test data with tuned hyperparameters
  
  Trained hyperparameters for Figure 1 Decision Tree algorithm are:
    k={'criterion': 'entropy', 'max_depth': 8, 'max_features': None, 'splitter': 'best'}
    75.625 -> Decision Tree test accuracy on future unseen test data with tuned hyperparameters
    
For Figure 1 the Decision Tree model performs better.
```

## Notes About Running the Program
***Ensure the GUI backend tk is installed.***
**tkinter** can be installed through the Linux bash terminal using the following command:
```
sudo apt install python3-tk
```
