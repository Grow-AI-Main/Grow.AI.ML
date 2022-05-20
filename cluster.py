from sklearn.cluster import KMeans
import pickle

class cluster:
    def __init__(self):
        with open('.\Models\km.pickle', 'rb') as f:
            self.km = pickle.load(f)

    
    def cluster(self, vec):
        cluster = self.km.predict(vec)