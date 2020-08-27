import scrapy
import re
from FashionScrapy.items import FashionscrapyItem
from FashionScrapy.spiders import CustomParser


class amazon_FashionScrapySpider(scrapy.Spider):
    # Define the spiders characteristics.
    name = 'amazon'
    allowed_domains = ['amazon.ca']
    start_urls = ['https://www.amazon.ca/DisplayPort-Axial-tech-technology-Auto-Extreme-DUAL-RTX2070/dp/B087YHYQV8/ref=sr_1_5?dchild=1&keywords=rtx+2070&qid=1598570207&sr=8-5']

    ###
    # Initialize the spider's paths.
    def __init__(self):
        self.declare_xpath()

    ###
    # Define all scrapable paths for the spider.
    def declare_xpath(self):
        self.getAllItemsXpath = "//*[@id='shopify-section-collection']/div/div/div/div[2]/div/div/div/div/div[2]/a/@href"
        self.CategoryXpath = "//*[@id='shopify-section-collection']/div/div/div/div[1]/h1/text()"
        self.TitleXpath = "//*[@id='shopify-section-collection']/div/div/div/div[2]/div/div/div/div/div[2]/a/div/div[1]/p/span[2]/text()"
        self.PriceXpath = "//*[@id='shopify-section-collection']/div/div/div/div[2]/div/div/div/div/div[2]/a/div/div/p/span/span[1]/text()"
        self.ImageXpath = "//*[@id='shopify-section-collection']/div/div/div/div[2]/div/div/div/div/div[1]/div/a/span/@data-bgset"

    ###
    # Find all products on page and crawl those items.
    def parse(self, response):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_main_item)

    ###
    # Parse the product page for declared xpaths.
    def parse_main_item(self, response):
        item = FashionscrapyItem()

        # Product URL for item in collection view
        ProductURL = response.xpath(self.getAllItemsXpath).extract()

        # Title
        Title = response.xpath(self.TitleXpath).extract()

        # Category
        Category = response.xpath(self.CategoryXpath).extract_first()

        # Price
        Price = response.xpath(self.PriceXpath).extract()

        # Iterate through all extracted images and add them to Images
        image_path = response.xpath(self.ImageXpath).extract()
        regex = r'\/\/(.*?).\[\(max'
        Images = []
        for image in image_path:
            matches = re.findall(regex, image)
            Images.append("https://" + matches[0])

        # Put each element into its item attribute.
        for itemURL, itemTitle, itemPrice, itemImage in zip(ProductURL, Title, Price, Images):
            item['Brand'] = self.brand
            item['ProductURL'] = response.urljoin(itemURL)
            item['Title'] = Category + " " + itemTitle
            item['Category'] = Category + " Sneaker"
            item['Price'] = itemPrice
            item['image_urls'] = [itemImage]
            item['Description'] = ""
            item['Size'] = []
            item['Colour'] = CustomParser().parse_for_colours(itemTitle)
            yield item
