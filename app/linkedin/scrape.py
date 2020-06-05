from linkedin_parser import LinkedinMainSearchPage, LinkedinSearchResult
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import numpy as np

search_keywords = 'energy engineer'
search_location = 'Los Angeles Metropolitan Area'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='/Users/rphamle/Desktop/Software/ChromeDriver/chromedriver', options=options) 

# Go directly to job search (no need to sign in)
url_base = 'https://www.linkedin.com/jobs/search/?'
url_vars = {
    'f_TPR' : 'r{0}'.format(24 * 60 * 60),  # last posted (in seconds), default: last 24 hours
    'keywords': search_keywords,
    'location': search_location,
}
main_search_page = LinkedinMainSearchPage.fromArgs(driver, url_base, url_vars)
time.sleep(np.random.uniform(2,4))

# Keep scrolling to the bottom until whole page is rendered
# Maybe there is a better way of doing this..
main_search_page.scrollWholePage()

# Find each job result
all_results = main_search_page.findJobResults()
print(len(all_results))