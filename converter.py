from numpy import NaN
import pandas as pd


class Converter:
    def convert_to_user_df(json):
        data = {}

        num_of_experiences = len(json['experiences'])

        for i in range(1, 9):
            if i <= num_of_experiences:
                data[f'Experience {i} Job Title'] = [json['experiences'][i - 1]['jobTitle']]
                data[f'Experience {i} Duration'] = [json['experiences'][i - 1]['duration']]

            else:
                data[f'Experience {i} Job Title'] = ['']
                data[f'Experience {i} Duration'] = [0]

        if 'firstDegree' in json:
            data['First Degree'] = [json['firstDegree']['type']]
            data['First Degree Field'] = [json['firstDegree']['field']]
            data['First Degree Institution Name'] = [json['firstDegree']['institutionName']]

        else:
            data['First Degree'] = ['']
            data['First Degree Field'] = ['']
            data['First Degree Institution Name'] = ['']

        if 'secondDegree' in json:
            data['Second Degree'] = [json['secondDegree']['type']]
            data['Second Degree Field'] = [json['secondDegree']['field']]
            data['Second Degree Institution Name'] = [json['secondDegree']['institutionName']]

        else:
            data['Second Degree'] = ['']
            data['Second Degree Field'] = ['']
            data['Second Degree Institution Name'] = ['']

        user_df = pd.DataFrame(data)

        return user_df
