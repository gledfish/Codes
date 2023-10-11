import csv
import scrapy


class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://new.qq.com/']

    def parse(self, response):
        # 提取新闻标题和链接
        links = response.css('a[href^="https://new.qq.com/rain/a/20230926A07BUW00"]')
        data = []
        for link in links:
            link_text = link.css('::text').get()
            link_url = link.attrib['href']
            data.append([link_text, link_url])

        # 保存到CSV文件
        with open('output.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'URL'])  # 写入表头
            writer.writerows(data)  # 写入数据
