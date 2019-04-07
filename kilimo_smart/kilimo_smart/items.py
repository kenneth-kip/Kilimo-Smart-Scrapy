# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PriceItem(scrapy.Item):
    # define the fields for your item here like:
    produce = scrapy.Field()
    location = scrapy.Field()
    quantity = scrapy.Field()
    low_price = scrapy.Field()
    high_price = scrapy.Field()
