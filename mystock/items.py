# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MystockItem(scrapy.Item):
    stock_num = scrapy.Field() # 종목코드
    max_price = scrapy.Field() # 최고가
    min_price = scrapy.Field() # 최저가
    current_price = scrapy.Field() # 현재가
    trading_volume = scrapy.Field() # 거래량
    create_at = scrapy.Field() # 데이터를 읽어온 시간