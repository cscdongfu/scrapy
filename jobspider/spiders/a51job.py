import scrapy


class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['51job.com']
    start_urls = [f'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E4%25BD%258E%25E7%25A2%25B3,2,{page}.html' for page in range(1,33)]



    def parse(self, response):

        # 提取数据
        # 提取url
        selectors = response.xpath('//div[@class="e"]')
        for selector in selectors:
            url = selector.xpath('./a/@href').get()

            print(url)










