import schedule
from spiders.mybots import MybotsSpider

schedule.every(10).minutes.do(MybotsSpider)