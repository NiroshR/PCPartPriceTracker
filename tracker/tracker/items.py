# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TrackerItem(scrapy.Item):
    # define the fields for your item here like:
    price = scrapy.Field()
    time = scrapy.Field()
    availability = scrapy.Field()
