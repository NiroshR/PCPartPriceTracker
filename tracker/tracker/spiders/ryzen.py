import scrapy
import re
from tracker.items import TrackerItem
from datetime import datetime


class Ryzen_FashionScrapySpider(scrapy.Spider):
    # Define the spiders characteristics.
    name = 'ryzen'
    allowed_domains = ['www.amazon.ca']
    start_urls = ['https://www.amazon.ca/gp/product/B07STGGQ18']

    # Need to supply a user agent so we don't get 503 error.
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    ###
    # Initialize the spider's paths.
    def __init__(self):
        self.declare_xpath()

    ###
    # Define all scrapable paths for the spider.
    def declare_xpath(self):
        self.AvailabilityXpath = "//*[@id='availability']/span/text()"
        self.PriceXpath = "//*[@id='priceblock_ourprice']/text()"

    ###
    # Find all products on page and crawl those items.
    def parse(self, response):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_main_item)

    ###
    # Parse the product page for declared xpaths.
    def parse_main_item(self, response):
        item = TrackerItem()

        # Availability
        Availability = response.xpath(self.AvailabilityXpath).extract_first()
        Availability = Availability.replace('\n', '').strip()

        # Price
        Price = response.xpath(self.PriceXpath).extract_first()
        Price = Price.replace('\n', '').strip()
        regex = r'(\d+\.\d{1,2})'
        Price = re.findall(regex, Price)[0]

        try:
            from datetime import timezone
        except ImportError:
            from scrapy.utils.python import timezone

        # Put each element into its item attribute.
        item['availability'] = Availability
        item['price'] = Price
        item['time'] = datetime.now(timezone.utc)
        return item
