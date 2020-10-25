# -*- coding: utf-8 -*-
import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['www.glassesshop.com']

    def start_requests(self):
        yield scrapy.Request(url='https://www.glassesshop.com/bestsellers/', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        })
    
    def parse(self, response):
        products = response.xpath("//div[@id='product-lists']/div")
        for product in products:
            yield {
                
                'name': product.xpath(".//div[@class='p-title']/a/@title").get(),
                'url': product.xpath(".//div[@class='product-img-outer']/a/@href").get(),
                'img_url': response.urljoin(product.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@src").get()),
                'price': product.xpath(".//div[@class='p-price']//span/text()").get(),
                'User-Agent': response.request.headers['User-Agent']
            }

        next_page = response.xpath("//ul[@class='pagination']/li[position() = last()]/a/@href").get()
        
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
            })
        