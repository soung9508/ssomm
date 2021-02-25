# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class MystockPipeline:
    def __init__(self):
        self.setupDBConnect()
        self.createTable()

    def process_item(self, item, spider):
        self.storeInDb(item)
        return item

    def storeInDb(self, item):
        stock_num=item.get('stock_num','').strip()
        max_price=item.get('max_price','').strip()
        min_price=item.get('min_price','').strip()
        current_price=item.get('current_price','').strip()
        trading_volume=item.get('trading_volume','').strip()
        create_at=item.get('create_at','').strip()

        sql = '''
        INSERT INTO mystock(stock_num, max_price,min_price, current_price, trading_volume, create_at)
        VALUES (%s,%s,%s,%s,%s,%s)
        '''
        #?의 값을 튜플로 받아서 해당 값을 넣어주는 작업
        self.cur.execute(sql, ( stock_num, max_price,min_price, current_price, trading_volume, create_at))
        self.conn.commit()

    def setupDBConnect(self):
        self.conn = pymysql.connect(host='127.0.0.1' , user= 'root', password= '1234', db='mystock', charset='utf8')   #self가 들어가는 앤 앨 다사용가능 
        self.cur= self.conn.cursor() #self없으면 로컬 변수
        print("DB Connected")

    def createTable(self) :
        self.cur.execute("DROP TABLE IF EXISTS mystock")


        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS mystock(
            stock_num VARCHAR(20) PRIMARY KEY,
            max_price VARCHAR(50) ,
            min_price VARCHAR(50) , 
            current_price  VARCHAR(100),
            trading_volume VARCHAR(100) , 
            create_at VARCHAR(20)
            ) DEFAULT CHARSET=UTF8 ''')