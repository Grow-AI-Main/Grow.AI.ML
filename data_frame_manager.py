from numpy import NaN
import pandas as pd
import os

from sqlalchemy import column

class DataFrameManager:
    def __init__(self):
        df = pd.read_csv(os.getcwd() + '/Data/data_custom_destination_job.csv')
        df.drop(['User Id'], axis=1, inplace=True)
        df = df.fillna('')

        self.df = df


    def get_data_frame(self):
        return self.df


    def filter_data_frame_by_destination_job(self, destination_job):
        data_frame_by_destination_job = self.df[self.df['destination_job'] == destination_job]
        data_frame_by_destination_job.reset_index(inplace=True)

        return data_frame_by_destination_job


    def get_unique_titles(self):
        columns = []

        for i in range(1, 9):
            columns.append(f'Experience {i} Job Title')

        titles = pd.unique(self.df[columns].values.ravel('K'))

        return list(titles)


    def get_unique_degree_types(self):
        degree_types = pd.unique(self.df[['First Degree', 'Second Degree']].values.ravel('K'))

        return list(degree_types)


    def get_unique_degree_fields(self):
        degree_fields = pd.unique(self.df[['First Degree Field', 'Second Degree Field']].values.ravel('K'))

        return list(degree_fields)


    def get_unique_degree_institutions(self):
        degree_institutions = pd.unique(self.df[['First Degree Institution Name', 'Second Degree Institution Name']].values.ravel('K'))

        return list(degree_institutions)