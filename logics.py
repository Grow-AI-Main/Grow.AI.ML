from typing_extensions import Self
import converter
import keras_model
import cluster
import recommendation
import numpy as np
import pandas as pd
import os

class logics:
    def __init__(self):
        self.converter = converter.converter()
        self.keras_model = keras_model.keras_model()
        self.cluster = cluster.cluster()
        self.recommendation = recommendation.recommendation()
        self.clusters = {}

        self.__load_clusters()


    def __load_clusters(self):
        df_path = os.getcwd() + '/Data/relevant_filterd_Data.csv'
        df = pd.read_csv(df_path)
        df.drop(['User Id'], axis=1, inplace=True)
        df = df.fillna('')

        items_features_dict = {name: np.array(value) for name, value in df.items()}

        encoded_items = self.keras_model.preprocess_and_encode(items_features_dict)

        predicts = self.cluster.predict(encoded_items)

        for i in range(9):
            self.clusters[i] = []

        for i in range(len(predicts)): 
            self.clusters[predicts[i]].append(i)


    def analyze_user(self, json):
        user_df = self.converter.convert_to_user_df(json)

        item_features_dict = {name: np.array(value) for name, value in user_df.items()}

        encoded_item = self.keras_model.preprocess_and_encode(item_features_dict)

        cluster = self.cluster.predict(encoded_item)

        return cluster