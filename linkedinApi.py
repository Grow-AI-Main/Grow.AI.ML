from linkedin_api import Linkedin


class LinkedinApi:
    def __init__(self):
        linkedinApi = Linkedin('ytal151@cs.colman.ac.il', 'yanivgmail5')
        self.linkedinApi = linkedinApi

    def get_profile_data(self, profileName):
        profile_data = self.linkedinApi.get_profile(public_id=profileName)
        return profile_data
