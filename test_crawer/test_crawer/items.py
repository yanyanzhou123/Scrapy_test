# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestCrawerItem(scrapy.Item):

    poetry_name = scrapy.Field()
    poetry_author = scrapy.Field()
    poetry_content = scrapy.Field()
    poetry_year = scrapy.Field()
