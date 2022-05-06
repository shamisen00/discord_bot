import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scraping.items import ScrapingItem

import yaml
from urllib.parse import urlparse, urljoin

with open('scraping/config.yml', 'r') as yml:
    url = yaml.safe_load(yml)

class ImagesSpider(CrawlSpider):
    name = 'images'
    allowed_domains = [urlparse(url["sample1"]["url"]).netloc]
    start_urls = [url["sample1"]["url"]]

    rules = (
        Rule(LinkExtractor(allow=( )), callback="parse_page", follow=True),
    )

    def parse_page(self, response):
        print("\n>>> Parse " + response.url + " <<<")
        # print(response.url.rsplit("/", 1)[0])
        item = ScrapingItem()
        item["image_directory_name"] = self.start_urls[0].rsplit("/", 1)[1]
        item["file_urls"] = []
        for image_url in response.css('a::attr("href")').re(r'.*.jpg'):
            if "http" not in image_url:
                item["file_urls"].append(response.url.rsplit("/", 1)[0] + "/" + image_url)
            else:
                item["file_urls"].append(image_url)
        # print(vars(item))
        return item

