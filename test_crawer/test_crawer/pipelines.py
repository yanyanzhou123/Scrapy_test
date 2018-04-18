# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlwt
import time
class TestCrawerPipeline(object):

    def __init__(self):
        self.workbook = ""
        self.worksheet = ""
        self.row = ""

    def open_spider(self,spider):
        """
        这里的代码代表爬虫刚开始的时候会执行,创建一个表格，并将该表和该sheet作为类内参数以便传递
        :param spider:
        :return:
        """
        print(time.localtime())
        self.workbook = xlwt.Workbook('kkk')
        self.worksheet = self.workbook.add_sheet('111')
        self.worksheet.write(0, 0, '诗词名')
        self.worksheet.write(0, 1, '朝代')
        self.worksheet.write(0, 2, '作者')
        self.worksheet.write(0, 3, '内容')
        self.row = 1

    def process_item(self, item, spider):
        """
        进行item筛选的地方，在这里面的动作会每次都被执行
        :param item:
        :param spider:
        :return:
        """
        poetry_list = list(item.values())
        self.write_in_excel(poetry_list)
        self.row = self.row + 1
        return item

    def close_spider(self,spider):
        '''
        这里的代码代表结束后执行
        :param spider:
        :return:
        '''
        self.workbook.save('kkk.xls')
        print(time.localtime())

    def write_in_excel(self, crawl_list):
        '''
        作为一种方法被调用
        :param crawl_list:
        :return:
        '''
        for col in range(len(crawl_list)):
            self.worksheet.write(self.row, col, crawl_list[col])


