# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy  # type: ignore


class Project1Item(scrapy.Item):
    # define the fields for your item here like:
    quote = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


# ---------------------------------------------------------------------------
# Extracted Data --> Temporary Containers (items) --> JSON/CSV/XML files
