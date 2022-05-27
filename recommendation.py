import numpy as np
from collections import Counter
from statistics import mean


class recommendation:
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
    def __find_average_duration(self, df, column, most_common_item):
        filtered_df = df[df[column] == most_common_item] 
        test_list_for_average = df[column].tolist()
        numerical_column_average = mean(test_list_for_average)
        rounded_average = round(numerical_column_average)
        return rounded_average


    # We'll loop everything to make it work on an entire dataframe
    def __create_recommended_job_dict(self, df):
        job_list= list()
        duration_list= list()
        for col in range (1,9):
            common_per_column = self.__find_most_common_item_in_column(df, f'Experience {col} Job Title')
            job_list.append(common_per_column)
            avg_duration_per_column = self.__find_average_duration(df, f'Experience {col} Duration', common_per_column)
            duration_list.append(avg_duration_per_column)
        recommended_job_and_duration_list = list(zip(job_list,duration_list))
        recommended_job_and_duration_dict = dict()
        for i in range(0,8):
            recommended_job_and_duration_dict.update({f"Recommended job {i+1}" : recommended_job_and_duration_list[i]})
        return recommended_job_and_duration_dict


    def __create_recommended_education_dict(self, df):
        recommended_first_degree_level = self.__find_most_common_item_in_column(df,'First Degree')
        recommended_second_degree_level =  self.__find_most_common_item_in_column(df,'Second Degree')
        recommended_first_degree_field = self.__find_most_common_item_in_column(df,'First Degree Field')
        recommended_second_degree_field =  self.__find_most_common_item_in_column(df,'Second Degree Field')
        recommended_first_degree_institution = self.__find_n_most_common_items_in_column(df, 'First Degree Institution Name')
        recommended_Second_degree_institution = self.__find_n_most_common_items_in_column(df, 'Second Degree Institution Name')
        recommended_education_list = dict()
        recommended_education_list.update({"Recommended First Degree Level" : recommended_first_degree_level})
        recommended_education_list.update({"Recommended First Degree Field" : recommended_first_degree_field})
        recommended_education_list.update({"Recommended top 3 First Degree Instituion" : recommended_first_degree_institution})
        recommended_education_list.update({"Recommended Second Degree Level" : recommended_second_degree_level})
        recommended_education_list.update({"Recommended Second Degree Field" : recommended_second_degree_field})
        recommended_education_list.update({"Recommended top 3 Second Degree Instituion" : recommended_Second_degree_institution})
        return recommended_education_list


    def __find_accomplished_education_items(self, cluster_df, user_input, recommeded_education_general):
        keys_to_remove = list()
        #in the case below - is when a person have studied the same degree as their allocated cluster - in one of three top places 
        if (user_input['First Degree Field'] == recommeded_education_general['Recommended First Degree Field'] and
        user_input['First Degree Institution Name'] in recommeded_education_general['Recommended top 3 First Degree Instituion']):
            keys_to_remove = ["Recommended First Degree Field","Recommended First Degree Level", "Recommended top 3 First Degree Instituion"]

        #in this case, if a person studied the right degree but in the wrong place,, we'll still drop the degree recommendation but add a note that says that
        elif (user_input['First Degree Field'] == recommeded_education_general['Recommended First Degree Field'] and
            user_input['First Degree Institution Name'] not in recommeded_education_general['Recommended top 3 First Degree Instituion']):
                recommeded_education_general.update({'Other First Degree Recommendations: the people who are similar to you studied at' : recommeded_education_general['Recommended top 3 First Degree Instituion']} )
                keys_to_remove = ["Recommended First Degree Field","Recommended First Degree Level", "Recommended top 3 First Degree Instituion"]

        #in the case below - the same goes for a second degree 
        if (user_input['Second Degree Field'] == recommeded_education_general['Recommended Second Degree Field'] and
        user_input['Second Degree Institution Name'] in recommeded_education_general['Recommended top 3 Second Degree Instituion']):
            keys_to_remove = ["Recommended Second Degree Level","Recommended First Degree Field","Recommended top 3 Second Degree Instituion"]

        elif (user_input['Second Degree Field'] == recommeded_education_general['Recommended Second Degree Field'] and
        user_input['Second Degree Institution Name'] not in recommeded_education_general['Recommended top 3 Second Degree Instituion']):
            recommeded_education_general.update({'Other Second Degree Recommendations: the people who are similar to you studied at' : recommeded_education_general['Recommended top 3 Second Degree Instituion']} )
            keys_to_remove = ["Recommended Second Degree Level","Recommended First Degree Field","Recommended top 3 Second Degree Instituion"]
        
        for key in keys_to_remove:
            del recommeded_education_general[key]
            
        return recommeded_education_general


    def __find_accomplished_job_items(self, cluster_df, user_input, recommeded_education_general):
        #gets a dataframe, another dataframe, and a dict 
        remove_from_recommendation_before_user = set()
        remove_from_user_input = set()  
        for i in range (1,9):
            for j in range (1,9):
                if user_input[f'Experience {i} Job Title'] == recommeded_education_general[f'Recommended job {j}'][0]:
                    remove_from_user_input.add(user_input[f'Experience {i} Job Title'])
                    remove_from_recommendation_before_user.add(f'Recommended job {j}')
        
        for key in remove_from_recommendation_before_user:
            del recommeded_education_general[key]

        return recommeded_education_general


    def __make_recommendation_json(self, education_recommendation, job_recommendation):
        firstDegree = {
            'type': education_recommendation[0],
            'field': education_recommendation[1],
            'institutionName' :  education_recommendation[2]
        } 

        secondDegree = {
            'type': education_recommendation[3],
            'field': education_recommendation[4],
            'institutionName' :  education_recommendation[5]
        }

        job_list = []
        for i in range (0, len(job_recommendation)):
            job = {
                'jobTitle': job_recommendation[i][0],
                'duration': job_recommendation[i][1]
            }
            job_list.append(job)

        recommendation = {
            'experiences': job_list,
            'firstDegree': firstDegree,
            'secondDegree': secondDegree
        }
        return recommendation


    def final_career_recommendation(self, assigned_cluster_df, user_input):
        #education:
        recommended_education_list_dict_before_user = self.__create_recommended_education_dict(assigned_cluster_df)
        final_education_recommendation = self.__find_accomplished_education_items(assigned_cluster_df, user_input, recommended_education_list_dict_before_user)
        final_education_list = [(k, v) for k, v in final_education_recommendation.items()]
        final_education_list_np = np.array(final_education_list)
        for i in range (0, len(final_education_list_np)):
            final_education_list_np = np.delete(final_education_list_np, [i])

        #jobs:
        recommended_job_list_dict_before_user = self.__create_recommended_job_dict(assigned_cluster_df)
        final_job_recommendation = self.__find_accomplished_job_items(assigned_cluster_df, user_input, recommended_job_list_dict_before_user)
        final_job_list = [(k, v) for k, v in final_job_recommendation.items()]
        final_job_list_np = np.array(final_job_list)
        for i in range (0, len(final_job_list_np)):
            final_job_list_np = np.delete(final_job_list_np, [i])

        recommendation = self.__make_recommendation_json(final_education_list_np, final_job_list_np)
        return recommendation