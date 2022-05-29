import converter
import keras_model
import knn
import recommendation
import data_frame_manager
import numpy as np

class Logics:
    def __init__(self):
        self.keras_model = keras_model.KerasModel()
        self.KNN = knn.KNN()
        self.recommendation = recommendation.Recommendation()
        self.data_frame_manager = data_frame_manager.DataFrameManager()
        self.supported_jobs = self.data_frame_manager.get_unique_destination_jobs()
        self.encoded_items_dict = {}

        self.__encode_items()


    def __encode_items(self):
        for supported_job in self.supported_jobs:
            df = self.data_frame_manager.filter_data_frame_by_destination_job(supported_job)

            items_features_dict = {name: np.array(value) for name, value in df.items()}

            encoded_items = self.keras_model.preprocess_and_encode(items_features_dict)

            self.encoded_items_dict[supported_job] = encoded_items


    def analyze_user(self, json):
        destination_job = json['destination_job']

        self.__verify_destination_job(destination_job)

        user_df = converter.Converter.convert_to_user_df(json)

        user_item_features_dict = {name: np.array(value) for name, value in user_df.items()}

        encoded_user_item = self.keras_model.preprocess_and_encode(user_item_features_dict)

        encoded_items = self.encoded_items_dict[destination_job]

        data_frame_by_destination_job = self.data_frame_manager.filter_data_frame_by_destination_job(destination_job)

        neighbors_df = self.KNN.get_neighbors(encoded_items, encoded_user_item, data_frame_by_destination_job, 18)

        user_input = {name: value for name, value in user_df.iloc[0].items()}

        recommend = self.recommendation.final_career_recommendation(neighbors_df, user_input)

        return recommend


    def __verify_destination_job(self, destination_job):
        if destination_job not in self.supported_jobs:
            raise ValueError(f'Not supported destination job: {destination_job}')