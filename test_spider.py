import requests
from lxml import etree
import xlwt
import time

def get_respone(url):

    res = requests.get(url).text
    response = etree.HTML(res)
    return response

def parse(response,row):
    poetry_list = response.xpath('//div[@class="left"]/div[@class ="sons"]')
    for poetry_info in poetry_list:
        poetry_name = poetry_info.xpath('./div/p/a/b/text()')[0]
        poetry_year = poetry_info.xpath('./div/p[@class="source"]/a[1]/text()')[0]
        poetry_author = poetry_info.xpath('./div/p[@class="source"]/a[2]/text()')[0]
        poetry_content_xp = poetry_info.xpath('./div/div[@class="contson"]')[0]
        poetry_content = poetry_content_xp.xpath('string()').replace('\n', '')
        poetry_info_list = [poetry_name,poetry_year,poetry_author,poetry_content]
        save_in_excel(poetry_info_list,row)
        row = row+1
    return row


def save_in_excel(crawl_list,row):
    for col in range(len(crawl_list)):
        worksheet.write(row, col, crawl_list[col])

if __name__ == '__main__':
    print (time.localtime())
    workbook = xlwt.Workbook('kkk')
    worksheet = workbook.add_sheet('111')
    worksheet.write(0, 0, '诗词名')
    worksheet.write(0, 1, '朝代')
    worksheet.write(0, 2, '作者')
    worksheet.write(0, 3, '内容')
    row = 1
    for page in range(1,50):
        url = 'https://www.gushiwen.org/default_{}.aspx'.format(page)
        res = get_respone(url)
        row = parse(res,row)

    workbook.save('kkk.xls')
    print(time.localtime())