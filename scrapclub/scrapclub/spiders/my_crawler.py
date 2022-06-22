import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MyCrawlerSpider(CrawlSpider):
    name = 'my_crawler'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="/html/body/div[3]/div/div[3]/div/div[3]/a"), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[@class='page-link']"), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//h4[@class='card-title']/a"), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath("//h3[@class='card-title']/text()").get()
        item['price'] = response.xpath("//h3[@class='card-title']/following-sibling::h4/text()").get()
        item['description'] = response.xpath("//p[@class='card-text']/text()").get()
        item['picture'] = response.xpath("//img[contains(@class, 'card-img-top')]/text()").get()
        yield item
