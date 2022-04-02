import scrapy

class PostsSpider(scrapy.Spider):
    name= "posts"
    page_number= str(2)
    start_urls=[
        'https://www.midsouthshooterssupply.com/dept/reloading/primers'
    ]

    def parse(self, response):
        urls=response.css('div.product > a::attr(href)').extract()
        for url in urls:
            url= response.urljoin(url)
            yield scrapy.Request(url=url,callback=self.parse_details)

        next_page_url="https://www.midsouthshooterssupply.com/dept/reloading/primers"+ PostsSpider.page_number + '/'
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse)
    
    def parse_details(self, response):
        if response.css('span.out-of-stock::text').extract_first() =='Out of Stock':
                stock= False
        else:
                stock=True

        info=str(response.xpath('//*[@id="delivery-info"]/ul/li').extract())
        info=info.replace("</li>', '<li>","__")
        info=info.replace("<li>","")
        info=info.replace("</li>","")
        yield {
            'price':response.css('span.price>span::text').extract_first(),
            'title':response.css('h1.product-name::text').extract_first(),
            'stock': stock,
            'manufacturer':response.css('div.catalog-item-brand-item-number>span a::text').extract_first(),
            'description':response.xpath('//*[@id="description"]/text()')[1].extract(),
            'delivery_info':info
           }