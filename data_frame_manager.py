import pandas as pd
import os


class DataFrameManager:
    def __init__(self):
        df = pd.read_csv(os.getcwd() + '/Data/filtered_data_many_titles.csv')
        df.drop(['User Id', 'index'], axis=1, inplace=True)
        df = df.fillna('')

        self.df = df


    def get_data_frame(self):
        return self.df


    def filter_data_frame_by_destination_job(self, destination_job):
        data_frame_by_destination_job = self.df[self.df['destination_job'] == destination_job]
        data_frame_by_destination_job.reset_index(inplace=True)

        return data_frame_by_destination_job


    def get_unique_destination_jobs(self):
        destination_jobs = pd.unique(self.df['destination_job'].values.ravel('K'))

        destination_jobs_list = list(destination_jobs)

        if '' in destination_jobs_list:
            destination_jobs_list.remove('')

        if 'Product Manager' in destination_jobs_list:
            destination_jobs_list.remove('Product Manager')
            
        destination_jobs_list.sort()

        return destination_jobs_list


    def get_unique_titles(self):
        columns = []

        for i in range(1, 9):
            columns.append(f'Experience {i} Job Title')

        titles = pd.unique(self.df[columns].values.ravel('K'))
        
        titles_list = list(titles)
        titles_list.remove('')
        titles_list.sort()

        return titles_list


    def get_unique_degree_types(self):
        degree_types = pd.unique(self.df[['First Degree', 'Second Degree']].values.ravel('K'))

        degree_types_list = list(degree_types)
        degree_types_list.remove('')
        degree_types_list.sort()

        return degree_types_list


    def get_unique_degree_fields(self):
        degree_fields = pd.unique(self.df[['First Degree Field', 'Second Degree Field']].values.ravel('K'))

        degree_fields_list = list(degree_fields)
        degree_fields_list.remove('')
        degree_fields_list.sort()

        return degree_fields_list


    def get_unique_degree_institutions(self):
        degree_institutions = pd.unique(self.df[['First Degree Institution Name', 'Second Degree Institution Name']].values.ravel('K'))

        degree_institutions_list = list(degree_institutions)
        degree_institutions_list.remove('')
        degree_institutions_list.sort()

        return degree_institutions_list


    def get_unique_degree_fields_by_degree_type(self, degree_type):
        filtered_df_by_degree_type = self.df[(self.df['First Degree'] == degree_type) | (self.df['Second Degree'] == degree_type)]
        degree_fields = pd.unique(filtered_df_by_degree_type[['First Degree Field', 'Second Degree Field']].values.ravel('K'))

        degree_fields_list = list(degree_fields)
        degree_fields_list.remove('')
        degree_fields_list.sort()

        return degree_fields_list


    def get_unique_degree_institutions_by_degree_type_and_degree_field(self, degree_type, degree_field):
        filtered_df_by_degree_type = self.df[(self.df['First Degree'] == degree_type) | (self.df['Second Degree'] == degree_type)]
        filtered_df_by_degree_type_and_degree_field = filtered_df_by_degree_type[(filtered_df_by_degree_type['First Degree Field'] == degree_field) | (filtered_df_by_degree_type['Second Degree Field'] == degree_field)]

        degree_institutions = pd.unique(filtered_df_by_degree_type_and_degree_field[['First Degree Institution Name', 'Second Degree Institution Name']].values.ravel('K'))

        degree_institutions_list = list(degree_institutions)
        degree_institutions_list.remove('')
        degree_institutions_list.sort()

        return degree_institutions_list
