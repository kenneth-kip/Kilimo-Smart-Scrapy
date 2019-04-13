# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from datetime import date
import base64

from scrapy.exporters import JsonItemExporter
from scrapy.conf import settings
from google.cloud import storage, exceptions


class KilimoSmartPipeline(object):
    def process_item(self, item, spider):
        return item

class KilimosmartPipeline(object):
    def process_item(self, item, spider):
        return item

class PricesJsonPipeline(object):
    credentials_file= "/credentials.json"

    def __init__(self):
        filename = date.today().strftime("%y_%m_%d") + '_prices.json'
        
        # Create tmp folder if does not exists.
        if not os.path.exists('tmp'):
            os.makedirs('tmp')

        self.file = open("tmp/" + filename, 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False, indent=1)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        self._upload_file(self.file.name)

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def _upload_file(self, filepath):
        self._create_gcs_credentials_file()
        client = storage.Client.from_service_account_json(os.getcwd() + self.credentials_file)
        bucket = client.get_bucket('kilimo-smart-scrapy-data')
        filename = "daily_prices/"+ filepath.split('/')[-1]
        blob2 = bucket.blob(filename)
        blob2.upload_from_filename(filename=filepath)
    
    def _create_gcs_credentials_file(self):
        try:
            credentials_file = open(os.getcwd() + self.credentials_file, "wb")
            encoded_string = base64.b64decode(settings['GCS_KEY_FILE'])
            credentials_file.write(encoded_string)
            credentials_file.close()
        except exceptions.NotFound:
            raise ValueError("ERROR: GCS bucket not found, path={}")
        except Exception as e:
            print(e)
        
