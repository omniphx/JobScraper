# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from JobScrape.items import JobscrapeItem

DOMAIN = 'surnames.behindthename.com'
URL = 'http://%s' % DOMAIN

class AcaciaSpider(scrapy.Spider):
    name = "acacia"
    allowed_domains = [DOMAIN]
    start_urls = (
        'http://acacia-inc.com/about-us/careers/',
    )

    def parse(self, response):
        for sel in response.xpath('//div[@class="entry-content"]/ul/li'):
            item = JobscrapeItem()
            item['company'] = 'Acacia'
            item['job'] = sel.xpath('a/text()').extract()[0]
            item['link'] = sel.xpath('a/@href').extract()[0]
            item['location'] = sel.xpath('text()').extract()[0]
            yield item