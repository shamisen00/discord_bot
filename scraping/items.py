# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class ScrapingItem((Item)):
    image_directory_name = Field()
    file_urls = Field()
    files = Field()
