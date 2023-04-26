import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering


# Runs the agglomerative_clustering algorithm
def agglomerative_clustering(data: list, fig_num):
    fig = plt.figure(figsize=(6, 6))
    plt.title("Dendrogram for Figure " + str(fig_num + 1))

    # Randomly shuffle the list of data
    np.random.shuffle(data)

    # Get all x values
    x_values = np.array([point[0][0] for point in data])

    # Get all y values
    y_values = np.array([point[0][1] for point in data])

    df = pd.DataFrame({"X": x_values, "Y": y_values})

    linkage_method = linkage(df, method='ward', metric='euclidean')
    dendro = dendrogram(linkage_method)

    # Show the plot
    plt.show(block=False)

    clusters = 0

    if fig_num == 0:
        clusters = 5
    elif fig_num == 1:
        clusters = 3
    elif fig_num == 2:
        clusters = 3
    elif fig_num == 3:
        clusters = 2
    elif fig_num == 4:
        clusters = 2
    elif fig_num == 5:
        clusters = 2

    cluster = AgglomerativeClustering(n_clusters=clusters, linkage='ward')

    # Visualizing the clustering
    plt.figure(figsize=(6, 6))
    plt.title("Clusters from Agglomerative Clustering for Figure " + str(fig_num + 1))
    plt.scatter(df['X'], df["Y"], c=cluster.fit_predict(df), cmap='rainbow')
    plt.show(block=False)

