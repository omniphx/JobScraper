# -*- coding: utf-8 -*-

# Scrapy settings for JobScrape project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'JobScrape'

SPIDER_MODULES = ['JobScrape.spiders']
NEWSPIDER_MODULE = 'JobScrape.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'JobScrape (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'JobScrape.pipelines.ValidatorPipeline': 0,
    'JobScrape.pipelines.JsonWriterPipeline': 1,
    'JobScrape.pipelines.StoreDataPipeline':2,
}

DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': 'mjmitchener',
            'password': 'root',
            'database': 'jobscraper'}