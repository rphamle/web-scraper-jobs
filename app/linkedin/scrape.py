from linkedin_parser import LinkedinMainSearchPage, LinkedinSearchResult
from linkedin_utilities import getResultInJson, writeResultToFile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
This script will
1) Start directly at the main page (job search results page)
2) Load all pages of results on the main (25 results per page)
3) Parse each result for key fields into JSON
4) Send to kafka topic
"""

search_keywords = 'energy engineer'
search_location = 'Los Angeles Metropolitan Area'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='/Users/rphamle/Desktop/Software/ChromeDriver/chromedriver', options=options) 

# "last posted" filter will be percent encoded
last_posted = {
    'last 24 hours': '1',
    'last week': '1,2',
    'last month': '1,2,3,4',
}
url_base = 'https://www.linkedin.com/jobs/search/?'
url_vars = {
    'f_TP' : last_posted['last week'],
    'keywords': search_keywords,
    'location': search_location,
    'distance': 50,     # in miles
}
# Go directly to job search (no need to sign in)
main_search_page = LinkedinMainSearchPage.fromArgs(driver, url_base, url_vars)

# Keep scrolling to the bottom until whole page is rendered
# Maybe there is a better way of doing this..
main_search_page.scrollWholePage()

# Find each job result
all_job_results = main_search_page.findJobResults(return_type = 'html')
print(len(all_job_results))

# (TEST) Get the main text body and job criteria categories
# Should put all these into a class or something
for i in range(0,1):
    url_job_result = all_job_results[i]['href']
    search_result = LinkedinSearchResult(driver, url_job_result)

    job_categories = search_result.findJobResultCategories(return_type = 'dict')
    job_description = search_result.findJobResultDescription(return_type = 'string')

    # Create the resulting job JSON
    result = getResultInJson(**job_categories, URL = url_job_result, Description = job_description)

    # Write to file
    filename = 'result_{0}.txt'.format(i + 1)
    writeResultToFile(result, filename, indent_level = 4)

# driver.quit()