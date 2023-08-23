# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapecpItem(scrapy.Item):
    Name=scrapy.Field()
    Link=scrapy.Field()
    pass
