# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from sqlalchemy.orm import sessionmaker
from models import Jobs, db_connect, create_jobs_table

from scrapy.exceptions import DropItem

class DuplicatePipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item

class ValidatorPipeline(object):
    def process_item(self, item, spider):
        if "Senior" in item['job']:
            return item
        else:
            raise DropItem("Senior jobs not allowed: %s" % item)

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('jobs.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4) + "\n"
        self.file.write(line)
        return item

class StoreDataPipeline(object):
    """Livingsocial pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates jobs table.
        """
        engine = db_connect()
        create_jobs_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save jobs in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        job = Jobs(**item)

        try:
            session.add(job)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item