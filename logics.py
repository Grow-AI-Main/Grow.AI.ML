import converter
import keras_model
import cluster
import recommendation
import data_frame_manager
import numpy as np

class Logics:
    def __init__(self):
        self.keras_model = keras_model.KerasModel()
        self.cluster = cluster.Cluster()
        self.recommendation = recommendation.Recommendation()
        self.clusters = {}

        self.__load_clusters()


    def __load_clusters(self):
        # Save DataFrame to self
        self.df = data_frame_manager.DataFrameManager().get_data_frame()

        items_features_dict = {name: np.array(value) for name, value in self.df.items()}

        encoded_items = self.keras_model.preprocess_and_encode(items_features_dict)

        predicts = self.cluster.predict(encoded_items)

        number_of_clusters = self.cluster.number_of_clusters()

        for i in range(number_of_clusters):
            self.clusters[i] = []

        for i in range(len(predicts)): 
            self.clusters[predicts[i]].append(i)


    def analyze_user(self, json):
        user_df = converter.Converter.convert_to_user_df(json)

        item_features_dict = {name: np.array(value) for name, value in user_df.items()}

        encoded_item = self.keras_model.preprocess_and_encode(item_features_dict)

        cluster = self.cluster.predict(encoded_item)

        similar_users = self.df.iloc[self.clusters[cluster[0]]]

        user_input = {name: value for name, value in user_df.iloc[0].items()}

        recommend = self.recommendation.final_career_recommendation(similar_users, user_input)

        return recommend