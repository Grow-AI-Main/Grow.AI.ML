from sklearn.cluster import KMeans
import pickle

class cluster:
    def __init__(self):
        with open('.\Models\km.pickle', 'rb') as f:
            self.km = pickle.load(f)


    def number_of_clusters(self):
        return self.km.n_clusters
        
    
    def predict(self, vec):
        cluster = self.km.predict(vec)
        return cluster