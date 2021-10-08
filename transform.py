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
        print(institution.pop('courses'))
        # for course in data['courses'][:]:
        #     print(course)

    for item in data['volunteer'][:]:
        data['volunteer'].remove(item)

    for job in reversed(data['work'][:]):
        if (job['name'] not in {'State Farm ®', 
                                    'Bank of America',
                                    'GM Financial'}):
            data['work'].remove(job)

    startDate = ''

    for i, job in enumerate(reversed(data['work'][:])):
        if (i % 2 == 0):
            startDate = job['startDate']
            data['work'].remove(job)
        else:
            job['startDate'] = startDate

    print(json.dumps(data, indent=4))
