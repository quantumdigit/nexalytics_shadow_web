import scrapy
 
class BootstrapTableSpider(scrapy.Spider):
    name = "bootstrap_table"
 
    def start_requests(self):
        urls = [
            'https://bitcoinchain.com/block_explorer/catalog',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        for row in response.xpath('//*[@class="table table-hover"]//tbody/tr'):
            yield {
                'Address' : row.xpath('td[1]//text()').extract_first(),
                'Hash': row.xpath('td[2]//text()').extract_first(),
            }
