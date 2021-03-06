# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SiweiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    R_id = scrapy.Field()
    R_name = scrapy.Field()
    length = scrapy.Field()
    start_name = scrapy.Field()
    end_name = scrapy.Field()
    dir = scrapy.Field()
    grade = scrapy.Field()
    pass
