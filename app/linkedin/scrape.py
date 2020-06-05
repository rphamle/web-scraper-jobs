from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import numpy as np
import urllib
from bs4 import BeautifulSoup

search_keywords = 'energy engineer'
search_location = 'Los Angeles Metropolitan Area'

class LinkedinBasePage():

    def __init__(self, driver, url):
        self.driver = driver
        self._goToUrl(url)

    @classmethod
    def fromArgs(cls, driver, url_base, url_args):
        return cls(driver, url_base + urllib.parse.urlencode(url_vars))

    def _goToUrl(self, url):
        self.driver.get(url)

    def _getSoup(self, **soup_args):
        # Get the entire html and pass to BeautifulSoup
        html_source = self.driver.page_source
        soup = BeautifulSoup(html_source, **soup_args)

        return soup

    def scrollWholePage(self):
        # Get length of current page
        script = "window.scrollTo(0, document.body.scrollHeight);var len_page=document.body.scrollHeight;return len_page;"
        len_page = self.driver.execute_script(script)

        # Loop until all pages rendered
        end = False
        while(end == False):
            previous_len_page = len_page
            time.sleep(np.random.uniform(2,4))
            len_page = self.driver.execute_script(script)

            if(previous_len_page == len_page):
                end = True

class LinkedinMainSearchPage(LinkedinBasePage):

    def findJobResults(self):
        soup = self._getSoup(features = 'html.parser')
        results = soup.find_all('a', class_ = 'result-card__full-card-link') 

        return results

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