# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = "demo"
    #allowed_domains = ["pyton123.io"]
    #start_urls = ['http://pyton123.io/ws/demo.html']
    urls=['http://python123.io/ws/demo.html']
    for url in urls:
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        fname=response.url.split('/')[-1]#文件名
        with open(fname,'wb')as f:
            f.write(response.body)
        self.log('saved file %s ' % fname)