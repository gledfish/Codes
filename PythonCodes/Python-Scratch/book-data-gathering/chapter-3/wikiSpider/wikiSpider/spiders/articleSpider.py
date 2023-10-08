from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article

class ArticleSpider(Spider):
    name =  "article"
    allowed_domains = ["http://pythonscraping.com"]
    start_urls = ["http://pythonscraping.com/pages/page3.html", "http://pythonscraping.com/pages/page2.html",  "http://pythonscraping.com/pages/page1.html"]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is:"  + title)
        item['title'] = title 
        return item