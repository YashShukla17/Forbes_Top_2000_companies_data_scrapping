import scrapy


class Top2000Spider(scrapy.Spider):
    name = 'top_2000'
    allowed_domains = ['www.forbes.com']
    start_urls = ['http://www.forbes.com/lists/global2000/']

    def parse(self, response):
        rows = response.xpath("//a[contains(@class,'table-row active')]")
        for row in rows:
            company_rank = row.xpath(".//div[@class='rank first table-cell  rank']/text()").get()
            Name = row.xpath(".//div[@class='organizationName second table-cell  name']/text()").get()
            country = row.xpath(".//div[@class='country  table-cell  country']/text()").get()
            market_value = row.xpath(".//div[@class='marketValue  table-cell  market value ']/text()").get()

            yield {
                'Company Rank': company_rank,
                'Organization Name': Name,
                'Country': country,
                'Market Value': market_value
            }

