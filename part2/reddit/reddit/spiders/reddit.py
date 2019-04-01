import scrapy
import re
from reddit.items import RedditItem

class RedditSpider(scrapy.Spider):
    name = 'reddit'
    allowed_domains = ['reddit.com']
    start_urls = ['http://www.reddit.com/']

    def parse(self, response):
	topics = response.xpath('//p[@class="title"]/a[@class="title may-blank"]/text()').extract()
	dates = response.xpath('//p[@class="tagline"]/time[@class="live-timestamp"]/@title').extract()
	comments = response.xpath('//div[@id="siteTable"]//a[@class="comments may-blank"]/@href').extract()
        for i, link in enumerate(comments):
            item = RedditItem()
            item['subreddit'] = str(re.findall('/r/[A-Za-z]*8?', link))[3:len(str(re.findall('/r/[A-Za-z]*8?', link)))-2]
            item['topic'] = topics[i]
            item['date'] = dates[i]
            yield item
