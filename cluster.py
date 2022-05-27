from sklearn.cluster import KMeans
import pickle

class Cluster:
    def __init__(self):
        with open('.\Models\km.pickle', 'rb') as f:
            self.kmeans = pickle.load(f)


    def number_of_clusters(self):
        return self.kmeans.n_clusters

    
    def predict(self, vec):
        cluster = self.kmeans.predict(vec)
        return cluster