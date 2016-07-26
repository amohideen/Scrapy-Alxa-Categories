# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from topnews.items import TopnewsItem


class AlexaSpider(CrawlSpider):
    name = 'alexa'
    allowed_domains = ['alexa.com']
    start_urls = ['http://www.alexa.com/topsites/category/Top/News']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[@class="alexa-pagination"]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
	selector = response.xpath('//*[@id="alx-content"]/div/div/section[2]/span/span/section/ul/li/div[2]/p/a/@href')
	for i in selector.extract():
		yield {"url": i.replace('/siteinfo/', 'www.')}
