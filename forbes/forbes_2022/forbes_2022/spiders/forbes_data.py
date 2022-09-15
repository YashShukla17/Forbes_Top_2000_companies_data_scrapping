import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ForbesDataSpider(CrawlSpider):
    name = 'forbes_data'
    allowed_domains = ['www.forbes.com']
    start_urls = ['http://www.forbes.com/lists/global2000/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='table-row-group']//a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #rank = response.xpath(".//a[@class='listuser-header__tag']/text()").get()
        company_name = response.xpath(".//div[@class='listuser-header__name']//@data-profile-name").get()
        Location = response.xpath(".//div[@class='listuser-header__headline--premium-location']/text()").get()
        Industry_type = response.xpath("(.//span[@class='profile-stats__text']/text())[1]").get()
        Founding_year = response.xpath("(.//span[@class='profile-stats__text']/text())[2]").get()
        Headquarters = response.xpath("(.//span[@class='profile-stats__text']/text())[3]").get()
        #operating_country = response.xpath("(.//span[@class='profile-stats__text']/text())[4]").get()
        CEO = response.xpath("(.//span[@class='profile-stats__text']/text())[5]").get()
        Employees = response.xpath("(.//span[@class='profile-stats__text']/text())[6]").get()
        #Financial_summary_year = response.xpath(".//div[@class='listuser-year__button']/@data-content").get()
        #Revenue = response.xpath("(.//div[@class='listuser-financial-item__value']/text())[1]").get()
        #Asset = response.xpath("(.//div[@class='listuser-financial-item__value']/text())[2]").get()
        #Profit = response.xpath("(.//div[@class='listuser-financial-item__value']/text())[3]").get()


        yield {
            "Company Name":company_name,
            "Location":Location,
            "Industry":Industry_type,
            "Founded":Founding_year,
            "Headquarters":Headquarters,
            "CEO":CEO,
            "Employees Number":Employees
        }
