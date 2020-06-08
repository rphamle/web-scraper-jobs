import time
import numpy as np
import urllib
from bs4 import BeautifulSoup
import json

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
        scroll_position = 0
        while True:
            # Get the height of the current page
            script = 'return document.body.scrollHeight'
            len_current_page = self.driver.execute_script(script)

            # Break if scroll position is at the bottom
            if(scroll_position == len_current_page):
                break

            # Scroll down in chunks (relative to each new page size) until end of the current page
            chunk_size = 4
            scroll_chunk = (len_current_page - scroll_position)/chunk_size
            while (scroll_position < len_current_page):
                script = "window.scrollTo(0, {0});".format(scroll_position + scroll_chunk)
                self.driver.execute_script(script)
                scroll_position += scroll_chunk
                time.sleep(np.random.uniform(0.5,1.5))
                
            time.sleep(np.random.uniform(2,4))

    @staticmethod
    def _returnResults(results, return_type):
        if(return_type == 'string' or return_type == 'text'):
            return results.text
        elif(return_type == 'jsons'):
            return json.dumps(results)
        else:
            # dict, json, html
            return results
    

class LinkedinMainSearchPage(LinkedinBasePage):

    def findJobResults(self, return_type):
        soup = self._getSoup(features = 'html.parser')
        results = soup.find_all('a', class_ = 'result-card__full-card-link') 

        return self._returnResults(results, return_type)

class LinkedinSearchResult(LinkedinBasePage):

    def findJobResultDescription(self, return_type):
        soup = self._getSoup(features = 'html.parser')
        results = soup.find_all('div', class_ = 'description__text')
        results = results[0]

        return self._returnResults(results, return_type)
    
    def findJobResultCategories(self, return_type):
        soup = self._getSoup(features = 'html.parser')
        results = soup.find_all('li', class_ = 'job-criteria__item')

        # Should be 4 categories:
        # Seniority level 
        # Employment type
        # Job function
        # Industries
        categories = {}
        for result in results:
            # Category name
            category_name = result.find('h3', class_ = 'job-criteria__subheader').text

            # Category value
            # 'Job Function' and 'Industries' can have multiple
            if(category_name == 'Job Function' or category_name == 'Industries'):
                category_values = result.find_all('span', class_ = 'job-criteria__text')
                categories[category_name] = [category_value.text for category_value in category_values]
            else:
                category_value = result.find('span', class_ = 'job-criteria__text')
                categories[category_name] = category_value.text

        return self._returnResults(categories, return_type)

