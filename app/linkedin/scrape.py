from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import numpy as np
import urllib

search_keywords = 'energy engineer'
search_location = 'Los Angeles Metropolitan Area'

def get_url(url_base, url_vars):
    return url_base + urllib.parse.urlencode(url_vars)

def renderWholePage(driver):
    # Get length of current page
    script = "window.scrollTo(0, document.body.scrollHeight);var len_page=document.body.scrollHeight;return len_page;"
    len_page = driver.execute_script(script)

    # Loop until all pages rendered
    end = False
    while(end == False):
        previous_len_page = len_page
        time.sleep(3)
        len_page = driver.execute_script(script)

        if(previous_len_page == len_page):
            end = True

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
jobs_url = get_url(url_base, url_vars)
driver.get(jobs_url)
time.sleep(1.1231)

# driver.quit()