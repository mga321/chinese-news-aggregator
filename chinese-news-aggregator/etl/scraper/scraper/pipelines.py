# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter
# import datetime
# import json




# NOTES for pipeline (below)

# YouTube Notes
# def __init__() to create connection
# def create_table() to create table


# MY NOTES
# Define an init function that runs every time the function is called, our init function will create a boto3 connection
# Define a process_item function that sends our data to S3

# Don't forget to add your pipeline to the ITEM_PIPELINES setting

class ScraperPipeline:

    def __init__(self):
        self.fp = open('scraped-data/china-daily-data.json', 'wb')
        self.exporter = JsonItemExporter(self.fp)
        self.exporter.start_exporting()
    

    def open_spider(self, spider):
        print('The crawler has started...')
    

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
    
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print('The crawler is done.')