
# coding: utf-8

# In[ ]:

import scrapy
from bs4 import BeautifulSoup

class WikipediaCrawler(scrapy.Spider):
    name = "wikipedia_crawler"
    start_urls = [
        'https://en.wikipedia.org/wiki/Luke_Skywalker'
    ]
    def parse(self, response):
        words = ["Galactic", "Empire", "galactic", "empire"]
        soup = BeautifulSoup(response.text, 'html.parser')
        div_main_content = soup.find('div', class_="mw-content-ltr")
        links = soup.find_all('a')
        if div_main_content != None:
            for word in words:
                if (div_main_content.find(string=word) != None):
                    print(response.url + " HAHAHA")
                    break
        
        if links != None:
            for link in links:
                href = link.get('href')
                yield scrapy.Request(response.urljoin(href), callback = self.parse)
        
        
        
            


# In[ ]:



