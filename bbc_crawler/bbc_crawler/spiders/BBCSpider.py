
# coding: utf-8

# In[ ]:
import scrapy
from scrapy.spiders import XMLFeedSpider
from bbc_crawler.items import BbcCrawlerItem
from bs4 import BeautifulSoup

class BBCSpider(XMLFeedSpider):
    name = 'testbbc'
    allowed_domains = ['bbc.co.uk', 'bbc.com', 'bbci.co.uk']
    start_urls = ['http://feeds.bbci.co.uk/news/world/rss.xml']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))

        item = BbcCrawlerItem()
        url = node.xpath('link/text()').extract()
        yield scrapy.Request(url[0], callback=self.parse_news)

    def parse_news(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        words = ["United States", "in US", "by US", "the US", "Trump", "Donald Trump", "Mike Pence", "Inauguration", "inauguration"]
        div_main = soup.find('div', class_="story-body")
        for word in words:
            if word in div_main.get_text():
                print(response.url + " hahaha")
                break

