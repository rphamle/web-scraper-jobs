from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import numpy as np

search_keywords = 'energy engineer'
search_location = 'Los Angeles Metropolitan Area'

def get_job_search_url(url_base, last_posted_in_seconds, search_keywords, search_location):
    # Get URL component for last posted
    if (last_posted_in_seconds == 'any_time'):
        url_last_posted = ''
    else:
        url_last_posted = 'f_TPR=r{0}'.format(last_posted_in_seconds)

    # Get URL component for search keywords
    url_keywords = 'keywords=' + search_keywords.replace(' ', '%20')

    # Get URL component for search location
    url_location = 'location=' + search_location.replace(' ', '%20')

    # Combine to form URL
    job_search_url = '&'.join([url_base, url_last_posted, url_keywords, url_location])

    return job_search_url

# specifies the path to the chromedriver.exe 
driver = webdriver.Chrome('/Users/rphamle/Desktop/Software/Chrome Driver/chromedriver') 

# Go directly to job search (no need to sign in)
url_base = 'https://www.linkedin.com/jobs/search/?'
last_posted_in_seconds = 24 * 60 * 60
jobs_url = get_job_search_url(url_base, last_posted_in_seconds, search_keywords, search_location)
driver.get(jobs_url)
time.sleep(1.1231)