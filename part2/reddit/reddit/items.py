# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RedditItem(scrapy.Item):
    date = scrapy.Field()
    author = scrapy.Field()
    topic = scrapy.Field()
    content = scrapy.Field()
    subreddit = scrapy.Field()

