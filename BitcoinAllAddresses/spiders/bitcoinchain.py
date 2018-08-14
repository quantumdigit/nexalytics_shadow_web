# -*- coding: utf-8 -*-
import scrapy


class BitcoinchainSpider(scrapy.Spider):
    name = 'bitcoinchain'
    allowed_domains = ['bitcoinchain.com']
    start_urls = ['http://bitcoinchain.com/']

    def parse(self, response):
        pass
