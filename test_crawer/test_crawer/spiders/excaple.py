# -*- coding: utf-8 -*-
import scrapy
from ..items import TestCrawerItem


class ExcapleSpider(scrapy.Spider):
    name = 'gushiwen'
    allowed_domains = ['gushiwen.org']
    start_urls = []#构造爬虫列表
    for page in range(1,500):
        start_urls.append('https://www.gushiwen.org/default_{}.aspx'.format(page))

    def parse(self, response):
        item = TestCrawerItem()
        poetry_list = response.xpath('//div[@class="left"]/div[@class ="sons"]')
        for poetry_info in poetry_list:
            item['poetry_name'] = poetry_info.xpath('./div/p/a/b/text()').extract_first()
            item['poetry_author'] = poetry_info.xpath('./div/p[@class="source"]/a[1]/text()').extract_first()
            item['poetry_year'] = poetry_info.xpath('./div/p[@class="source"]/a[2]/text()').extract_first()
            poetry_content_xp = poetry_info.xpath('./div/div[@class="contson"]')
            item['poetry_content'] = poetry_content_xp.xpath('string()').extract_first().replace('\n','')
            # print(item['poetry_name'],item['poetry_author'],item['poetry_year'],item['poetry_content'])
            yield item

