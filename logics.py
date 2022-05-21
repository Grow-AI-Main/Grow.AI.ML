import keras_model
import cluster
import numpy as np
import pandas as pd

class logics:
    def __init__(self):
        self.keras_model = keras_model()
        self.cluster = cluster()
        self.clusters = {}

        load_clusters(self)


def load_clusters(self):
    df = pd.read_csv('.\Data\relevant_filterd_Data.csv')
    df.drop(['User Id'], axis=1, inplace=True)
    df = df.fillna('')

    items_features_dict = {name: np.array(value) for name, value in df.items()}

    encoded_items = self.keras_model.preprocess_and_encode(items_features_dict)

    predicts = self.cluster.predict(encoded_items)

    for i in range(9):
        self.clusters[i] = []

    for i in range(len(predicts)): 
        self.clusters[predicts[i]].append(i)