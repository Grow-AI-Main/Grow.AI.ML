import time

class LinkedinApi:

    def get_profile_data(self, profile_name):
        
        if profile_name != 'tom-pony' and profile_name != 'gal-tandeitnik':
            raise ValueError(f'Not supported profile name: {profile_name}')

        time.sleep(0.5)

        if profile_name == 'tom-pony':
            profile_data = {
                'experiences': [
                    {
                        'jobTitle': 'Software Developer',
                        'companyName': 'IDF - Unit 8200',
                        'duration': 12,
                        'startDate': {
                            'year': 2017,
                            'month': ''
                        },
                        'endDate': {
                            'year': 2018,
                            'month': ''
                        }
                    },
                    {
                        'jobTitle': 'QA',                        
                        'companyName': 'IDF - Unit 8200',
                        'duration': 12,
                        'startDate': {
                            'year': 2018,
                            'month': ''
                        },
                        'endDate': {
                            'year': 2019,
                            'month': ''
                        }
                    },
                    {
                        'jobTitle': 'Software Developer',                        
                        'companyName': 'IDF - Unit 8200',
                        'duration': 28,
                        'startDate': {
                            'year': 2019,
                            'month': 'Jan'
                        },
                        'endDate': {
                            'year': 2021,
                            'month': 'Apr'
                        }
                    },
                    {
                        'jobTitle': 'Software Developer',                        
                        'companyName': 'SysAid',
                        'duration': 12,
                        'startDate': {
                            'year': 2021,
                            'month': 'Jul'
                        },
                        'endDate': {
                            'year': 2022,
                            'month': 'Jun'
                        }
                    }
                ],
                'firstDegree': {
                    'type': 'B.Sc.',
                    'field': 'Computer Science',
                    'institutionName': 'College of Management '
                }
            }
            return profile_data

        if profile_name == 'gal-tandeitnik':
            profile_data = {
                'experiences': [
                    {
                        'jobTitle': 'Software Developer',
                        'companyName': 'IDF - Unit 8200',
                        'duration': 45,
                        'startDate': {
                            'year': 2016,
                            'month': 'Jun'
                        },
                        'endDate': {
                            'year': 2020,
                            'month': 'Feb'
                        }
                    },
                    {
                        'jobTitle': 'Software Developer',                        
                        'companyName': 'IDF - Unit 8200',
                        'duration': 16,
                        'startDate': {
                            'year': 2021,
                            'month': 'Mar'
                        },
                        'endDate': {
                            'year': 2022,
                            'month': 'Jun'
                        }
                    }
                ],
                'firstDegree': {
                    'type': 'B.Sc.',
                    'field': 'Computer Science',
                    'institutionName': 'College of Management '
                }
            }
            return profile_data