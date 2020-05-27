from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import numpy as np
import urllib

search_keywords = 'energy engineer'
search_location = 'Los Angeles Metropolitan Area'

def get_url(url_base, url_vars):
    return url_base + urllib.parse.urlencode(url_vars)

# specifies the path to the chromedriver.exe 
driver = webdriver.Chrome('/Users/rphamle/Desktop/Software/Chrome Driver/chromedriver') 

# Go directly to job search (no need to sign in)
url_base = 'https://www.linkedin.com/jobs/search/?'
url_vars = {
    'f_TPR' : 'r{0}'.format(24 * 60 * 60),  # last posted (in seconds), default: last 24 hours
    'keywords': search_keywords,
    'location': search_location,
}
jobs_url = get_url(url_base, url_vars)
driver.get(jobs_url)
time.sleep(1.1231)

# driver.quit()