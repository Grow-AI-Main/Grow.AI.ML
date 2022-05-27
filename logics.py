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
        self.keras_model = keras_model.keras_model()
        self.cluster = cluster.cluster()
        self.recommendation = recommendation.recommendation()
        self.clusters = {}

        self.__load_clusters()


    def __load_clusters(self):
        df = pd.read_csv(os.getcwd() + '/Data/relevant_filterd_Data.csv')
        df.drop(['User Id'], axis=1, inplace=True)
        df = df.fillna('')

        items_features_dict = {name: np.array(value) for name, value in df.items()}

        # Save DataFrame to self
        self.df = df

        encoded_items = self.keras_model.preprocess_and_encode(items_features_dict)

        predicts = self.cluster.predict(encoded_items)

        number_of_clusters = self.cluster.number_of_clusters()

        for i in range(number_of_clusters):
            self.clusters[i] = []

        for i in range(len(predicts)): 
            self.clusters[predicts[i]].append(i)


    def analyze_user(self, json):
        user_df = converter.converter.convert_to_user_df(json)

        item_features_dict = {name: np.array(value) for name, value in user_df.items()}

        encoded_item = self.keras_model.preprocess_and_encode(item_features_dict)

        cluster = self.cluster.predict(encoded_item)

        similar_users = self.df.iloc[self.clusters[cluster[0]]]

        user_input = {name: value for name, value in user_df.iloc[0].items()}

        recommend = self.recommendation.final_career_recommendation(similar_users, user_input)

        return recommend