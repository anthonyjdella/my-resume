import json

with open('resume-pre-transform.json') as json_data:
    data = json.load(json_data)

    for project in data['projects'][:]:
        if (project['name'] not in {'JSON Resume using LinkedIn', 
                                    'www.AnthonyDellavecchia.com',
                                    'Automated Job Scraping'}):
            data['projects'].remove(project)
    
    for reference in data['references'][:]:
        data['references'].remove(reference)
    
    for language in data['languages'][:]:
        data['languages'].remove(language)

    for institution in data['education'][:]:
        if (institution['institution'] == 'The University of Texas at Austin'):
            data['education'].remove(institution)
        institution.pop('courses')

    for item in data['volunteer'][:]:
        data['volunteer'].remove(item)

    for skill in data['skills'][:]:
        data['skills'].remove(skill)

    for job in reversed(data['work'][:]):
        if (job['name'] not in {'State Farm ®', 
                                'Bank of America',
                                'GM Financial'}):
            data['work'].remove(job)
        else:
            job['location'] = 'Dallas, TX'

    start_date = ''
    highlights = {}

    for i, job in enumerate(reversed(data['work'][:])):
        if (i % 2 == 0):
            start_date = job['startDate']
            data['work'].remove(job)
        else:
            job['startDate'] = start_date
            highlights[i] = job['summary']
            job['summary'] = ''

    gmf = []
    boa = []
    sf  = []

    for highlight in highlights:
        if (highlight == 1):
            for i, item in enumerate(highlights[highlight].split('\n\n')):
                gmf.append(item)
                data['work'][2].update({'highlights': gmf})
        elif (highlight == 3):
            for i, item in enumerate(highlights[highlight].split('\n\n')):
                boa.append(item)
                data['work'][1].update({'highlights': boa})
                data['work'][1].update({'position': 'Applications Programmer'})
        elif (highlight == 5):
            for i, item in enumerate(highlights[highlight].split('\n\n')):
                sf.append(item)
                data['work'][0].update({'highlights': sf})
                data['work'][0].update({'position': 'Software Developer'})

    # Change element name from url to website
    data['basics']['website'] = data['basics'].pop('url')
    data['basics']['website'] = 'https://www.anthonydellavecchia.com'

    data['basics']['image'] = 'https://www.anthonydellavecchia.com/images/contact/avatar2.png'

    current = ['Java', 'Python', 'Git', 'CI/CD', 'Spring Boot', 'JUnit', 'Cucumber', 'Unix']
    skill_current = {'name': 'Current Experience', 'level': '', 'keywords': current}

    prior = ['Node.js', 'JavaScript', 'HTML', 'CSS', 'ETL', 'SQL', 'UI/UX Design']
    skill_prior = {'name': 'Prior Experience', 'level': '', 'keywords': prior}

    # tools = ['Git', 'Zsh', 'IntelliJ', 'VS Code']
    # skill_tools = {'name': 'Tools', 'level': '', 'keywords': tools}

    engineering = ['Data Structures', 'Algorithms', 'Systems Design', 'Agile SDLC']
    skill_engineering = {'name': 'Engineering', 'level': '', 'keywords': engineering}
    
    data['skills'].append(skill_current)
    data['skills'].append(skill_prior)
    # data['skills'].append(skill_tools)
    data['skills'].append(skill_engineering)

    data['meta'].update({'theme': 'caffeine'})

    print(json.dumps(data, indent=4))
