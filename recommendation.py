import numpy as np
from collections import Counter
from statistics import mean
import json
import pandas as pd


class Recommendation:
    # That's how we find out the most occuring item in a column
    def __find_most_common_item_in_column(self, df, column):
        df_after_droping_naans = df.drop(df[df[column] == ''].index)
        column_list = df_after_droping_naans[column].tolist()
        most_common_item = max(column_list, key = column_list.count)
        return most_common_item

    def __find_n_most_common_items_in_column(self, df, column):
        df_after_droping_naans = df.drop(df[df[column] == ''].index)
        column_list = df_after_droping_naans[column].tolist()
        most_common_n_items = Counter(column_list)
        college_list_with_num_of_appearances = most_common_n_items.most_common(3)
        college_only_list = list()
        college_only_list.append(college_list_with_num_of_appearances[0][0])
        college_only_list.append(college_list_with_num_of_appearances[1][0])
        college_only_list.append(college_list_with_num_of_appearances[2][0])
        return college_only_list

    # We'll choose the most common item, filter the data by it, and calculate the average number of months
    # for people who did this role on their K job
    def __find_average_duration(self, df, experience_column, duration_column, most_common_item):
        filtered_df = df[df[experience_column] == most_common_item]
        test_list_for_average = df[duration_column].tolist()
        numerical_column_average = mean(test_list_for_average)
        rounded_average = round(numerical_column_average)
        return rounded_average

    # We'll loop everything to make it work on an entire dataframe
    def __create_recommended_job_dict(self, df):
        job_list= list()
        duration_list= list()
        recommended_job_and_duration_list = list()
        for col in range (1,9):
            common_per_column = self.__find_most_common_item_in_column(df, f'Experience {col} Job Title')
            job_list.append(common_per_column)
            avg_duration_per_column = self.__find_average_duration(df, f'Experience {col} Job Title', f'Experience {col} Duration', common_per_column)
            duration_list.append(avg_duration_per_column)
        recommended_job_and_duration_list = list(zip(job_list,duration_list))
        recommended_job_and_duration_dict = dict()
        for i in range(0,8):
            recommended_job_and_duration_dict.update({f"Recommended job {i+1}" :(job_list[i], duration_list[i])})
        return recommended_job_and_duration_dict

    def __create_recommended_education_dict(self, neighbours_df):
        recommended_first_degree_level = self.__find_most_common_item_in_column(neighbours_df, 'First Degree')
        recommended_second_degree_level = self.__find_most_common_item_in_column(neighbours_df, 'Second Degree')
        recommended_first_degree_field = self.__find_most_common_item_in_column(neighbours_df, 'First Degree Field')
        recommended_second_degree_field = self.__find_most_common_item_in_column(neighbours_df, 'Second Degree Field')
        recommended_first_degree_institution = self.__find_n_most_common_items_in_column(neighbours_df, 'First Degree Institution Name')
        recommended_second_degree_institution = self.__find_n_most_common_items_in_column(neighbours_df, 'Second Degree Institution Name')
        recommended_first_degree = dict()
        recommended_second_degree = dict()

        recommended_first_degree.update({"Recommended First Degree Level": recommended_first_degree_level})
        recommended_first_degree.update({"Recommended First Degree Field": recommended_first_degree_field})
        recommended_first_degree.update({"Recommended top 3 First Degree Instituions": recommended_first_degree_institution})
        recommended_second_degree.update({"Recommended Second Degree Level": recommended_second_degree_level})
        recommended_second_degree.update({"Recommended Second Degree Field": recommended_second_degree_field})
        recommended_second_degree.update({"Recommended top 3 Second Degree Instituions": recommended_second_degree_institution})

        return recommended_first_degree, recommended_second_degree

    def __find_accomplished_education_items(self, user_input_df, recommended_first_degree, recommended_second_degree):
        keys_to_update_first = []
        keys_to_update_second = []

        # in the case below - is when a person have studied the same degree as their allocated cluster - in one of three top places
        if ((user_input_df['First Degree Field'][0] == recommended_first_degree['Recommended First Degree Field']) &
        (user_input_df['First Degree Institution Name'][0] in recommended_first_degree['Recommended top 3 First Degree Instituions'])):
            keys_to_update_first = ["Recommended First Degree Field", "Recommended First Degree Level", "Recommended top 3 First Degree Instituions"]

        # in the case below - the same goes for a second degree
        if ((user_input_df['Second Degree Field'][0] == recommended_second_degree['Recommended Second Degree Field']) &
        (user_input_df['Second Degree Institution Name'][0] in recommended_second_degree['Recommended top 3 Second Degree Instituions'])):
            keys_to_update_second = ["Recommended Second Degree Level", "Recommended First Degree Field", "Recommended top 3 Second Degree Instituions"]

        for key in keys_to_update_first:
            del recommended_first_degree[key]

        for key in keys_to_update_second:
            del recommended_second_degree[key]

        return recommended_first_degree, recommended_second_degree

    def __find_accomplished_job_items(self, user_input_df,recommended_job_dict_before_user):
        # gets a dataframe, another dataframe, and a dict
        update_from_recommendation_before_user = set()
        update_from_user_input = set()
        index_to_delete_in_general_recommendation = set()
        index_to_delete_in_user = set()
        for i in range(1, 9):
            for j in range(1, 9):
                if user_input_df[f'Experience {i} Job Title'][0] == recommended_job_dict_before_user[f'Recommended job {j}'][0]:
                    index_to_delete_in_general_recommendation.add(j)
                    index_to_delete_in_user.add(i)
                    update_from_user_input.add(user_input_df[f'Experience {i} Job Title'][0])
                    update_from_recommendation_before_user.add(f'Recommended job {j}')

        index_to_delete_in_user_list = list(index_to_delete_in_user)
        index_to_delete_in_general_recommendation_list = list(index_to_delete_in_general_recommendation)
        index_to_delete_in_general_recommendation_list.sort()

        indices_to_delete = list()
        for i in range(0, len(index_to_delete_in_user_list)):
            indices_to_delete.append(index_to_delete_in_general_recommendation_list[-i - 1])

        for k in indices_to_delete:
            del recommended_job_dict_before_user[f'Recommended job {k}']

        return recommended_job_dict_before_user

    def __cut_recommendation_after_dream_job(sel, job_recommendation_after_user, user_destination_job):

        job_list = list()
        job_list = list(job_recommendation_after_user.items())
        delete_from_here = 0
        flag = 0
        for i in range(0, len(job_list)):
            if job_list[i][1][0] == user_destination_job:
                delete_from_here = i + 1
                flag = 1
                break

        if (flag == 1):
            del job_list[delete_from_here:len(job_list)]

        final_job_dict = dict()
        for i in range(0, len(job_list)):
            final_job_dict.update({job_list[i][0]: (job_list[i][1][0], job_list[i][1][1])})
        return final_job_dict

    def __make_recommendation_json(self, first_deg_education_after_user, second_deg_education_after_user,job_rec_after_achieving_detination_job):

        recommendation = dict()
        firstDegree = dict()
        secondDegree = dict()
        job_dict = dict()
        if first_deg_education_after_user:
            firstDegree = {
                'type': first_deg_education_after_user['Recommended First Degree Level'],
                'field': first_deg_education_after_user['Recommended First Degree Field'],
                'institutionName': first_deg_education_after_user['Recommended top 3 First Degree Instituions']
            }

        if second_deg_education_after_user:
            secondDegree = {
                'type': second_deg_education_after_user['Recommended Second Degree Level'],
                'field': second_deg_education_after_user['Recommended Second Degree Field'],
                'institutionName': second_deg_education_after_user['Recommended top 3 Second Degree Instituions']
            }

        if job_rec_after_achieving_detination_job:
            job_list = list(job_rec_after_achieving_detination_job.items())
            job_list_dict = list()
            for i in range(0, len(job_list)):
                job = {
                    'jobTitle': job_list[i][1][0],
                    'duration': job_list[i][1][1]
                }
                job_list_dict.append(job)
        if firstDegree:
            recommendation = {
                'experiences': job_list_dict,
                'first education recommendation': firstDegree,
                'second education recommendation': secondDegree
            }
        if not firstDegree:
            recommendation = {
                'experiences': job_list_dict,
                'first education recommendation': secondDegree
            }
        if not firstDegree and not secondDegree:
            recommendation = {
                'experiences': job_list_dict
            }
        return recommendation

    def __final_career_recommendation_json(self, neighbours_df, user_input_dict, user_destination_job):
        user_input_df = self.__from_dict_to_df(user_input_dict)
        recommended_first_degree, recommended_second_degree = self.__create_recommended_education_dict(neighbours_df)
        recommended_job_list_dict_before_user = self.__create_recommended_job_dict(neighbours_df)
        first_deg_education_after_user, second_deg_education_after_user = self.__find_accomplished_education_items(
            user_input_df, recommended_first_degree, recommended_second_degree)
        final_job_recommendation = self.__find_accomplished_job_items(user_input_df, recommended_job_list_dict_before_user)
        # print(final_job_recommendation)
        job_rec_after_achieving_destination_job = self.__cut_recommendation_after_dream_job(final_job_recommendation, user_destination_job)
        final_career_recommendation = self.__make_recommendation_json(first_deg_education_after_user,second_deg_education_after_user,job_rec_after_achieving_detination_job)

        return final_career_recommendation

