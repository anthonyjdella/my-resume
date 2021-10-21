# Anthony Dellavecchia's Resume

This hosts my resume, which is written in JSON.

### Why JSON?

Being able to update my resume in a developer friendly format (JSON) is nice because it is one "source of truth".
When I make an update to the JSON, I can display it in multiple styles instead of having to create multiple resumes.

This is much more convinient than LaTeX!

## Contents
* `resume-pre-transform.json` is the raw JSON extracted from LinkedIn, using the [Chrome Extension tool](https://github.com/anthonyjdella/customized-linkedin-to-jsonresume). 
* `transform.py` is a Python script to take the contents from `resume-pre-transform.json` and transform the data to fit my resume needs.
* `resume.json` is the output after running `transform.py`. This is my resume in JSON format, which I use to apply multiple themes.

## Run
`python3 transform.py`
