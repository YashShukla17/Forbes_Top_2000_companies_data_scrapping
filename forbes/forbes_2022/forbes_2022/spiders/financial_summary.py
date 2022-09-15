import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ForbesDataSpider(CrawlSpider):
    name = 'financial_summary'
    allowed_domains = ['www.forbes.com']
    start_urls = ['http://www.forbes.com/lists/global2000/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='table-row-group']//a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #rank = response.xpath(".//a[@class='listuser-header__tag']/text()").get()
        company_name = response.xpath(".//div[@class='listuser-header__name']//@data-profile-name").get()
        Financial_summary_year = response.xpath(".//div[@class='listuser-year__button']/@data-content").get()
        Revenue = response.xpath("(.//div[@class='listuser-financial-item__value']/text())[1]").get()
        Asset = response.xpath("(.//div[@class='listuser-financial-item__value']/text())[2]").get()
        Profit = response.xpath("(.//div[@class='listuser-financial-item__value']/text())[3]").get()


        yield {
            "Company Name":company_name,
            "Year":Financial_summary_year,
            "Revenue":Revenue,
            "Asset":Asset,
            "Profit":Profit
        }
