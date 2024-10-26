# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def serialize_price(value:str) -> str:
    return f"$ {value}"

class BookItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    product_type = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()
    number_of_reviews = scrapy.Field()
    stars = scrapy.Field()
    description = scrapy.Field()
    
