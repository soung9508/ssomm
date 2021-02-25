import scrapy
from mystock.items import MystockItem
from scrapy.http import Request
from datetime import datetime


class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['finance.naver.com/item/sise.nhn?code=005930']
    start_urls = ['http://finance.naver.com/item/sise.nhn?code=005930']

    def parse(self, response):
        stock_nums=response.xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]/text()').extract()
        max_prices=response.xpath('//*[@id="_high"]/text()').extract()
        min_prices=response.xpath('//*[@id="_low"]/text()').extract()
        current_prices=response.xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[4]/td[2]/span/text()').extract()
        trading_volumes=response.xpath('//*[@id="_quant"]/text()').extract()
        create_ats=response.xpath('//*[@id="time"]/em/text()').extract()
       
        items =[]
        for i in range(len(stock_nums)) :
            item= MystockItem()
            item ['stock_num'] = stock_nums[i]
            item ['max_price'] = max_prices[i]
            item ['min_price'] = min_prices[i]
            item ['current_price'] = current_prices[i]
            item ['trading_volume'] = trading_volumes[i]
            item ['create_at'] = create_ats[i]
            items.append(item)

        return items


