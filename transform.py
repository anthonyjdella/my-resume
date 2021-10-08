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

    print(json.dumps(data, indent=4))