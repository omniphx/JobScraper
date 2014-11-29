# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    job = scrapy.Field()
    link = scrapy.Field()
    location = scrapy.Field()
    pass
