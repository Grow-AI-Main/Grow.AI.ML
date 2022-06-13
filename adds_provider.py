import random

class AddsProvider:
    def provide_jobs_adds(self, destination_job):
        adds = []
    
        if destination_job == 'Software Developer Team Lead':
            software_developer_team_lead = [
                {
                    "jobTitle": "Software Engineering Intern",
                    "companyName": "SAP",
                    "description": "",
                    "link": "https://jobs.sap.com/job/Ra&apos;anana-Intern-Software-Developer-%28Student%29-SAP-BTP-Portal-Services-4366202/809468701/"
                },
                {
                    "jobTitle": "Software Engineering Intern",
                    "companyName": "F5",
                    "description": "",
                    "link": "https://ffive.wd5.myworkdayjobs.com/en-US/f5jobs/job/Tel-Aviv/Software-Engineer-Intern---NAP-ML--python_RP1025812-1"
                },
                {
                    "jobTitle": "Software Engineer - Machine Learning Intern ",
                    "companyName": "Verily",
                    "description": "",
                    "link": "https://verily.com/careers/job/?gh_src=verily&job_id=3813059"
                },
                {
                    "jobTitle": "Software Engineering Intern",
                    "companyName": "Qualcomm",
                    "description": "",
                    "link": "https://qualcomm.dejobs.org/haifa-isr/sw-engineering-intern-qualcomm-haifa-israel/45EC5A43DE3D43D7B03E3F9CABE6C7C9/job/"
                },
                {
                    "jobTitle": "Fullstack Engineer",
                    "companyName": "Wix",
                    "description": "",
                    "link": "https://www.wix.com/jobs/locations/tel-aviv/positions/217001?val=software-engineer-israel"
                },
                {
                    "jobTitle": "Software Engineer",
                    "companyName": "Amazon",
                    "description": "",
                    "link": "https://www.amazon.jobs/en/jobs/2084779/software-development-engineer-cloudendure"
                },
                {
                    "jobTitle": "Software Engineer",
                    "companyName": "Spectory",
                    "description": "",
                    "link": "https://boards.greenhouse.io/onedigital/jobs/5376790002"
                },
                {
                    "jobTitle": "Software Engineer",
                    "companyName": "Medcase",
                    "description": "Senior Software Engineer",
                    "link": "https://www.medcase.health/corporate-openings/senior-software-engineer"
                }
            ]
            adds.extend(software_developer_team_lead)

        elif destination_job == 'Data Scientist':
            data_scientist_adds = [
                {
                    "jobTitle": "Software Engineering Intern",
                    "companyName": "SAP",
                    "description": "",
                    "link": "https://jobs.sap.com/job/Ra&apos;anana-Intern-Software-Developer-%28Student%29-SAP-BTP-Portal-Services-4366202/809468701/"
                },
                {
                    "jobTitle": "Software Engineering Intern",
                    "companyName": "F5",
                    "description": "",
                    "link": "https://ffive.wd5.myworkdayjobs.com/en-US/f5jobs/job/Tel-Aviv/Software-Engineer-Intern---NAP-ML--python_RP1025812-1"
                },
                {
                    "jobTitle": "Software Engineer - Machine Learning Intern ",
                    "companyName": "Verily",
                    "description": "",
                    "link": "https://verily.com/careers/job/?gh_src=verily&job_id=3813059"
                },
                {
                    "jobTitle": "Software Engineering Intern",
                    "companyName": "Qualcomm",
                    "description": "",
                    "link": "https://qualcomm.dejobs.org/haifa-isr/sw-engineering-intern-qualcomm-haifa-israel/45EC5A43DE3D43D7B03E3F9CABE6C7C9/job/"
                },
                {
                    "jobTitle": "Fullstack Engineer",
                    "companyName": "Wix",
                    "description": "",
                    "link": "https://www.wix.com/jobs/locations/tel-aviv/positions/217001?val=software-engineer-israel"
                },
                {
                    "jobTitle": "Software Engineer",
                    "companyName": "Amazon",
                    "description": "",
                    "link": "https://www.amazon.jobs/en/jobs/2084779/software-development-engineer-cloudendure"
                },
                {
                    "jobTitle": "Software Engineer",
                    "companyName": "Spectory",
                    "description": "",
                    "link": "https://boards.greenhouse.io/onedigital/jobs/5376790002"
                },
                {
                    "jobTitle": "Software Engineer",
                    "companyName": "Medcase",
                    "description": "Senior Software Engineer",
                    "link": "https://www.medcase.health/corporate-openings/senior-software-engineer"
                },
                {
                    "jobTitle": "Data Science Student",
                    "companyName": "Intel",
                    "description": "",
                    "link": "https://jobs.intel.com/ShowJob/Id/3362937/Data-Scientist-student?wapkw=data%20science%20student%20israel"
                },
                {
                    "jobTitle": "Data Analyst",
                    "companyName": "Data Analyst",
                    "description": "No elaboration",
                    "link": "https://boards.greenhouse.io/embed/job_app?for=doubleverify&token=6178822002&b=https%3A%2F%2Fwww.doubleverify.com%2Fcareers%2F"
                },
                {
                    "jobTitle": "Data Analyst",
                    "companyName": "Natural Intelligence",
                    "description": "Business data analyst",
                    "link": "https://www.naturalint.com/jobs/co/analytics/A9.D22/business-data-analyst/all/"
                },
                {
                    "jobTitle": "Data Analyst",
                    "companyName": "Sorbet",
                    "description": "Junior Data Analyst",
                    "link": "https://www.comeet.com/jobs/sorbet/17.002/junior-data-analyst/47.D23"
                },
                {
                    "jobTitle": "Data Integration Engineer",
                    "companyName": "Optimove",
                    "description": "Data Integration Engineer",
                    "link": "https://www.optimove.com/careers/data-science-analytics/7A.C10/data-integration-engineer"
                },
                {
                    "jobTitle": "QA",
                    "companyName": "Hexa3d",
                    "description": "Junior QA Tester",
                    "link": "https://www.hexa3d.io/careers/?jobId=34.E23"
                },
                {
                    "jobTitle": "QA",
                    "companyName": "InGima",
                    "description": "QA Engineer",
                    "link": "https://www.ingima.com/qa-engineers/?lang=en"
                },
                {
                    "jobTitle": "QA",
                    "companyName": "Sapiens",
                    "description": "QA Automation Tester",
                    "link": "https://careers.sapiens.com/job/Holon-QA-Automation-Tester/802016201/"
                },
            ]
            adds.extend(data_scientist_adds)

        else:
            raise ValueError(f'Not supported adds for destination job: {destination_job}')

        selected_adds = random.sample(adds, 3)
        return selected_adds


    def provide_educations_adds(self, degree_type):
        educations = [
            {
                "type": "B.Sc.",
                "field": "Computer Science",
                "institutionName": "College of Management",
                "link": "https://www.colman.ac.il/academics/ba/computer-science/"
            },
            {
                "type": "B.Sc.",
                "field": "Computer Science",
                "institutionName": "Tel Aviv University",
                "link": "https://go.tau.ac.il/he/exact/ba/computer"
            },
            {
                "type": "B.Sc.",
                "field": "Computer Science",
                "institutionName": "Ben Gurion University of the Negev",
                "link": "https://in.bgu.ac.il/welcome/Pages/degree_1/nature/Computer_Science_degree_1.aspx"
            },
            {
                "type": "B.Sc.",
                "field": "Computer Science",
                "institutionName": "Hebrew University of Jerusalem",
                "link": "https://info.huji.ac.il/bachelor/Computer-Sciences"
            },
            {
                "type": "B.Sc.",
                "field": "Computer Science",
                "institutionName": "Reichman University",
                "link": "https://www.runi.ac.il/schools/computer-science/undergraduate/ba/"
            },
            {
                "type": "M.Sc.",
                "field": "Computer Science",
                "institutionName": "Ben Gurion University of the Negev",
                "link": "https://in.bgu.ac.il/advanced/Pages/nature/cs.aspx"
            },
            {
                "type": "M.Sc.",
                "field": "Computer Science",
                "institutionName": "Tel Aviv University",
                "link": "https://go.tau.ac.il/he/exact/ma/computer"
            },
            {
                "type": "M.Sc.",
                "field": "Computer Science",
                "institutionName": "Reichman University",
                "link": "https://www.runi.ac.il/schools/computer-science/graduate/msc/"
            },
            {
                "type": "M.Sc.",
                "field": "Computer Science",
                "institutionName": "Hebrew University of Jerusalem",
                "link": "https://info.huji.ac.il/master/Computer-Sciences"
            },
            {
                "type": "B.A.",
                "field": "Business",
                "institutionName": "Ben Gurion University of the Negev",
                "link": "https://in.bgu.ac.il/fom/BusinessDep/Pages/default.aspx"
            },
            {
                "type": "B.A.",
                "field": "Business",
                "institutionName": "Reichman University",
                "link": "https://www.runi.ac.il/schools/business/undergraduate/"
            },
            {
                "type": "B.A.",
                "field": "Business",
                "institutionName": "College of Management",
                "link": "https://www.colman.ac.il/academics/ba/business-administration/"
            },
            {
                "type": "B.A.",
                "field": "Business",
                "institutionName": "Emek Yizrael College",
                "link": "https://www.yvc.ac.il/%D7%9E%D7%A1%D7%9C%D7%95%D7%9C%D7%99-%D7%9C%D7%99%D7%9E%D7%95%D7%93/b-a-%D7%A8%D7%91-%D7%AA%D7%97%D7%95%D7%9E%D7%99/%D7%A0%D7%99%D7%94%D7%95%D7%9C-%D7%A2%D7%A1%D7%A7%D7%99-%D7%95%D7%AA%D7%A2%D7%A9%D7%99%D7%99%D7%AA%D7%99/"
            },
            {
                "type": "B.A.",
                "field": "Business",
                "institutionName": "Tel Aviv University",
                "link": "https://coller.tau.ac.il/"
            },
            {
                "type": "M.B.A.",
                "field": "Business",
                "institutionName": "Reichman University",
                "link": "https://www.runi.ac.il/admissions/graduate/registration/business-mba/"
            },
            {
                "type": "M.B.A.",
                "field": "Business",
                "institutionName": "College of Management",
                "link": "https://www.colman.ac.il/academics/ma/m-b-a-business-administration/"
            },
            {
                "type": "M.B.A.",
                "field": "Business",
                "institutionName": "Tel Aviv University",
                "link": "https://coller.tau.ac.il/"
            },
            {
                "type": "M.B.A.",
                "field": "Business",
                "institutionName": "Hebrew University of Jerusalem",
                "link": "https://bschool.huji.ac.il/"
            },
            {
                "type": "M.B.A.",
                "field": "Business",
                "institutionName": "Ben Gurion University of the Negev",
                "link": "https://in.bgu.ac.il/advanced/Pages/management/business-management.aspx"
            },
        ]

        filtered_educations = list(filter(lambda x: x['type'] == degree_type, educations))

        selected_educations = random.sample(filtered_educations, 3)

        return selected_educations

