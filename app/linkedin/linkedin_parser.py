import time
import numpy as np
import urllib
from bs4 import BeautifulSoup

class LinkedinBasePage():

    def __init__(self, driver, url):
        self.driver = driver
        self._goToUrl(url)

    @classmethod
    def fromArgs(cls, driver, url_base, url_vars):
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

class LinkedinSearchResult(LinkedinBasePage):

    def findJobResultBody(self):
        soup = self._getSoup(features = 'html.parser')
        results = soup.find_all('div', class_ = 'description__text')

        return results
    
    def findJobResultCategories(self):
        soup = self._getSoup(features = 'html.parser')
        results = soup.find_all('li', class_ = 'job-criteria__item')

        return results