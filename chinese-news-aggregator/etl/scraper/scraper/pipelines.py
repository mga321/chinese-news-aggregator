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
        self.fp = open('json.json', 'wb')
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
    

    # def start_exporting(self):
    #     self.file.write(b"[")
    #     self._beautify_newline()
    

    # def finish_exporting(self):
    #     self._beautify_newline()
    #     self.file.write(b"]")
    

    # def export_item(self, item):
    #     if self.first_item:
    #         self.first_item = False
    #     else:
    #         self.file.write(b",")
    #         self._beautify_newline()
        
    #     itemdict = dict(self._get_serialized_fields(item))
    #     data = self.encoder.encode(itemdict)
    #     self.file.write(to_bytes(data, self.encoding))


    # def process_item(self, item, spider):

    #     exporter = JsonItemExporter('data/file-name-here.json')
    #     exporter.start_exporting()
    #     exporter.export_item(item)
    #     exporter.finish_exporting()

    #     return item