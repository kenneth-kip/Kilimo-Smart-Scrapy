# -*- coding: utf-8 -*-
import scrapy

from scrapy.selector import Selector
from kilimo_smart.items import PriceItem


class PriceFetcherSpider(scrapy.Spider):
    name = 'price_fetcher'
    allowed_domains = ['mfarm.co.ke']
    start_urls = ['https://mfarm.co.ke/trends']

    def parse(self, response):
        selector = Selector(response=response)
        for price in selector.xpath('/html/body/div[2]/div[2]/div[1]/div/table//tbody/tr').getall():
            item = Selector(text=price).xpath('//tr/td/text()').extract()
            price_item = PriceItem()
            price_item['produce'] = item[0]
            price_item['location'] = item[1]
            price_item['quantity'] = item[2].split()[0]
            price_item['low_price'] = item[3]
            price_item['high_price'] = item[4]
            yield price_item