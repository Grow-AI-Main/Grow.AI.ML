import numpy as np
from collections import Counter
from statistics import mean
import json
import pandas as pd


class Recommendation:

    def __dict_to_df(self, user_input_dict):
        user_input_df_new = pd.DataFrame.from_dict(user_input_dict)
        return user_input_df_new

    # This function gets the dataframe of neighbours and a colum name
    # drops the rows where there's now values and finds the most common item in a colomn
    # returns the name of the item as string
    def __find_most_common_itme_in_current_column(neighbours_df, column):
        df_after_droping_naans = neighbours_df.drop(neighbours_df[neighbours_df[column] == ''].index)
        column_list = df_after_droping_naans[column].tolist()
        most_common_item = max(column_list, key=column_list.count)
        return most_common_item

    # this function gets the neighbours dataframe and a column name
    # and finds the most common 3 items
    # return a list of the 3 most common items
    def __find_three_most_common_items_in_current_column(self, neiboughrs_df, column):
        top_three_colleges = []

        df_after_droping_naans = neiboughrs_df.drop(neiboughrs_df[neiboughrs_df[column] == ''].index)
        colums_of_df = df_after_droping_naans[column].tolist()
        most_common_three_items_in_column = Counter(colums_of_df)
        college_name_and_num_of_appearnces = most_common_three_items_in_column.most_common(3)
        top_three_colleges.append(college_name_and_num_of_appearnces[0][0])
        top_three_colleges.append(college_name_and_num_of_appearnces[1][0])
        top_three_colleges.append(college_name_and_num_of_appearnces[2][0])

        return top_three_colleges

    # This function gets the K nearest neighbours dataframe, a job title column and job duration coloumn and the most common item in the
    # job title column
    # it finds the average duration of the most common job in the job column
    # returns the rounded avarage - number of months
    def __find_average_duration_of_common_job(self, neighbours_df, experience_column, duration_column, most_common_item):
        # make a df with only the common job title
        filtered_df = neighbours_df[neighbours_df[experience_column] == most_common_item]
        durations = filtered_df[duration_column].tolist()
        column_average = mean(durations)
        rounded_average = round(column_average)
        return rounded_average

    # this function gets the k nearest neighbours dataframe
    # find the most common items in each job column and the average duration of each job
    # returns a recommedation dictionairy as if the user did not work in anything
    def __create_recommended_job_dict(self, neiboughrs_df):
        jobs = []
        durations = []
        recommended_jobs_and_durations = dict()
        num_of_job_columns = 8

        for column in range(1, num_of_job_columns + 1):
            comon_job_per_column = self.__find_most_common_itme_in_current_column(neiboughrs_df,
                                                                           f'Experience {column} Job Title')
            jobs.append(comon_job_per_column)
            avg_duration_per_job = self.__find_average_duration_of_common_job(neiboughrs_df, f'Experience {column} Job Title',
                                                                       f'Experience {column} Duration',
                                                                       comon_job_per_column)
            durations.append(avg_duration_per_job)

        for column in range(0, num_of_job_columns):
            recommended_jobs_and_durations.update({f"Recommended job {column + 1}": (jobs[column], durations[column])})
        return recommended_jobs_and_durations

    # This function gets the k nearest neighbours dataframe
    # finds the most common item in the degree feild & degree type columns
    # and finds the top 3 most common items in the instituion column
    # and returns the recommendation as if the user did not study anything so far
    def __create_recommended_education_dict(self, neighbours_df):
        recommended_first_degree = dict()
        recommended_second_degree = dict()

        # find the most common items in the field, type and top 3 in the instituion columns
        recommended_first_degree_level = self.__find_most_common_itme_in_current_column(neighbours_df, 'First Degree')
        recommended_second_degree_level = self.__find_most_common_itme_in_current_column(neighbours_df, 'Second Degree')
        recommended_first_degree_field = self.__find_most_common_itme_in_current_column(neighbours_df, 'First Degree Field')
        recommended_second_degree_field = self.__find_most_common_itme_in_current_column(neighbours_df, 'Second Degree Field')
        recommended_first_degree_institution = self.__find_most_common_itme_in_current_column(neighbours_df,
                                                                                              'First Degree Institution Name')
        recommended_Second_degree_institution = self.__find_three_most_common_items_in_current_column(neighbours_df,
                                                                                               'Second Degree Institution Name')

        # create two dictionaries with the recommended educations
        recommended_first_degree.update({"Recommended First Degree Level": recommended_first_degree_level})
        recommended_first_degree.update({"Recommended First Degree Field": recommended_first_degree_field})
        recommended_first_degree.update(
            {"Recommended top 3 First Degree Instituions": recommended_first_degree_institution})
        recommended_second_degree.update({"Recommended Second Degree Level": recommended_second_degree_level})
        recommended_second_degree.update({"Recommended Second Degree Field": recommended_second_degree_field})
        recommended_second_degree.update(
            {"Recommended top 3 Second Degree Instituions": recommended_Second_degree_institution})
        return recommended_first_degree, recommended_second_degree

    # this function gets the k nearest neighbours dataframe, the recommended first and second degree
    # as if the user did not study anything yet
    # it comapares the general education recommendation to what the user have already studied
    # and returns the recommendation after taking out what the user have already studied - of the first and second degrees
    def __find_accomplished_education_items(self,user_input_df, recommended_first_degree, recommended_second_degree):
        keys_to_delete_first_degree = []
        keys_to_delete_second_degree = []
        users_first_degree_field = user_input_df['First Degree Field'][0]
        users_second_degree_field = user_input_df['Second Degree Field'][0]
        users_first_degree_institution = user_input_df['First Degree Institution Name'][0]
        users_second_degree_institution = user_input_df['Second Degree Institution Name'][0]
        recommended_first_degree_field = recommended_first_degree['Recommended First Degree Field']
        recommended_second_degree_field = recommended_second_degree['Recommended Second Degree Field']
        recommended_first_degree_top_three_institutions = recommended_first_degree[
            'Recommended top 3 First Degree Instituions']
        recommended_second_degree_top_three_institutions = recommended_second_degree[
            'Recommended top 3 Second Degree Instituions']

        # in the case below - is when a person have studied the same degree as their allocated cluster - in one of three top places
        if ((users_first_degree_field == recommended_first_degree_field) &
                (users_first_degree_institution in recommended_first_degree_top_three_institutions)):
            keys_to_delete_first_degree = ["Recommended First Degree Field", "Recommended First Degree Level",
                                           "Recommended top 3 First Degree Instituions"]
        # take all theses out in varibales - explample - user degree

        # in the case below - the same goes for a second degree
        if ((users_second_degree_field == recommended_second_degree_field) &
                (users_second_degree_institution in recommended_second_degree_top_three_institutions)):
            keys_to_delete_second_degree = ["Recommended Second Degree Level", "Recommended First Degree Field",
                                            "Recommended top 3 Second Degree Instituions"]

        for key in keys_to_delete_first_degree:
            del recommended_first_degree[key]

        for key in keys_to_delete_second_degree:
            del recommended_second_degree[key]

        return recommended_first_degree, recommended_second_degree

    # this function gets the k nearest neighbours df and the recommneded jobs and durations
    # as if the user had never worked
    # it finds the jobs the user had already done and gets them off the recommendation
    # for example - if the general recommendation is to do 3 software jobs, and the user have done 1, it will recommend 2 jobs (what's left)
    # returns the final job recommendation
    def __find_accomplished_job_items(self, user_input_df, recommended_job_dict_before_user):

        indices_to_delete_in_general_recommendation = set()
        indices_to_delete_in_user_input = set()
        num_of_job_columns = 8

        for i in range(1, num_of_job_columns + 1):
            for j in range(1, num_of_job_columns + 1):
                # if the user does a job that exists in any of the existing recommendation columns
                if user_input_df[f'Experience {i} Job Title'][0] == \
                        recommended_job_dict_before_user[f'Recommended job {j}'][0]:
                    # add the relevant index to delete later in the general recommendation
                    indices_to_delete_in_general_recommendation.add(j)
                    indices_to_delete_in_user_input.add(i)

        # turn the sets to list - so it will be iterable
        index_to_delete_in_user_list = list(indices_to_delete_in_user_input)
        index_to_delete_in_general_recommendation_list = list(indices_to_delete_in_general_recommendation)
        # sorting the list for deleting the n jobs from the end of the recommendation
        index_to_delete_in_general_recommendation_list.sort()

        indices_to_delete = list()
        for i in range(0, len(index_to_delete_in_user_list)):
            indices_to_delete.append(index_to_delete_in_general_recommendation_list[-i - 1])

        for k in indices_to_delete:
            del recommended_job_dict_before_user[f'Recommended job {k}']

        return recommended_job_dict_before_user

    # this function gets the job & education recommendations after cutting what the user have already achieved
    # cuts the job & duration recommendation after the user have achvied their dream job
    # returns the final job recommedation that ends witht with the dream job
    def __cut_recommendation_after_dream_job(self, job_recommendation_after_user, user_destination_job):
        jobs_recommendation_after_user_jobs = list()
        jobs_recommendation_after_user_jobs = list(job_recommendation_after_user.items())
        num_of_jobs_after_user_jobs = len(jobs_recommendation_after_user_jobs)
        delete_from_here = 0
        flag = 0

        for i in range(0, num_of_jobs_after_user_jobs):
            # if the current job title is the user's destination job
            if jobs_recommendation_after_user_jobs[i][1][0] == user_destination_job:
                # remember the index of this title and raise flag
                delete_from_here = i + 1
                flag = 1
                break

        if (flag == 1):
            # delete all the job recommendations after acheiving the dream job
            del jobs_recommendation_after_user_jobs[delete_from_here:num_of_jobs_after_user_jobs]

        updated_num_of_jobs_after_user_jobs = len(jobs_recommendation_after_user_jobs)
        final_job_recommendation = dict()
        for i in range(0, updated_num_of_jobs_after_user_jobs):
            final_job_recommendation.update({jobs_recommendation_after_user_jobs[i][0]: (
            jobs_recommendation_after_user_jobs[i][1][0], jobs_recommendation_after_user_jobs[i][1][1])})
        return final_job_recommendation

    # this function gets the final education & job recommendations (the job recommendation after achieving the dream job)
    # it turns all these into one json in order to send it to the client
    # return an organized json
    def __make_recommendation_json(self,first_deg_education_recommendation, second_deg_education_recommedation,
                                 job_rec_after_achieving_detination_job):

        recommendation = dict()
        firstDegree = dict()
        secondDegree = dict()
        jobs = dict()

        # if the first degree recommendation is not empty
        if first_deg_education_recommendation:
            firstDegree = {
                'type': first_deg_education_recommendation['Recommended First Degree Level'],
                'field': first_deg_education_recommendation['Recommended First Degree Field'],
                'institutionName': first_deg_education_recommendation['Recommended top 3 First Degree Instituions']
            }

        # if the second degree recommendation is not empty
        if second_deg_education_recommedation:
            secondDegree = {
                'type': second_deg_education_recommedation['Recommended Second Degree Level'],
                'field': second_deg_education_recommedation['Recommended Second Degree Field'],
                'institutionName': second_deg_education_recommedation['Recommended top 3 Second Degree Instituions']
            }
        # if the job recommendation is not empty
        if job_rec_after_achieving_detination_job:
            # turn the job dict into list so it will be iterable
            job_list = list(job_rec_after_achieving_detination_job.items())
            job_dict = list()
            for i in range(0, len(job_list)):
                job = {
                    'jobTitle': job_list[i][1][0],
                    'duration': job_list[i][1][1]
                }
                job_dict.append(job)

        # if there's no recommedation - don't add it
        # if there's only a second degree recommedation - add it only
        if firstDegree:
            recommendation = {
                'experiences': job_dict,
                'first education recommendation': firstDegree,
                'second education recommendation': secondDegree
            }
        if not firstDegree:
            recommendation = {
                'experiences': job_dict,
                'first education recommendation': secondDegree
            }
        if not firstDegree and not secondDegree:
            recommendation = {
                'experiences': job_dict
            }
        return recommendation

    # this is the final function that activates all the functions
    # only need to call this function
    # it gets the k nearest neigbouts dataframe, the user input and the user destination job
    # and returns the final recommendation json


    def final_career_recommendation_json(self, neighbours_df, user_input_dict, user_destination_job):
        # turn the user input input from json to dataframe
        user_input_df = self.__dict_to_df(user_input_dict)

        # get the general first & second degree recommendations - as if the user studied nothing
        recommended_first_degree, recommended_second_degree = self.__find_most_common_itme_in_current_column(neighbours_df)

        # get the general job title & duration recommendation - as if the user worked at nothing
        recommended_job_list_dict_before_user = self.__create_recommended_job_dict(neighbours_df)

        # get the first & second degree recommendation after cutting what the user has already studied
        first_deg_education_after_user, second_deg_education_after_user = self.__find_accomplished_education_items(user_input_df,
                                                                                                            recommended_first_degree,
                                                                                                            recommended_second_degree)

        # get the job title & duration recommendation after cutting what the user have already worked at
        job_recommendation_after_user = self.__find_accomplished_job_items(user_input_df, recommended_job_list_dict_before_user)

        # get the job title & duration recommendation after cutting what's after the user have achived their dream job
        final_job_recommendation = self.__cut_recommendation_after_dream_job(job_recommendation_after_user, user_destination_job)

        # get a json with the job & education recommendations combined
        final_career_recommendation = self.__make_recommendation_json(first_deg_education_after_user,
                                                               second_deg_education_after_user, final_job_recommendation)

        return final_career_recommendation
