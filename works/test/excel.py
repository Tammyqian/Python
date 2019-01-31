# -*- coding:utf-8 -*-
import  xlsxwriter
import numpy as np
from io import BytesIO
from urllib2 import urlopen

def get_xy(row,col):
    table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num1 = col/26
    num2 = col%26
    if num1 == 0:
        return (table[num2-1]+str(row))
    else:
        return (table[num1-1]+table[num2-1]+str(row))

def main():
    # img = np.array('./images/photo1.jpeg')
    # rows,cols,dims = img.shape
    # print img.shape
    # print img.dtype
    # print img.size
    # print type(img)

    exce = xlsxwriter.Workbook('images_bytesio.xlsx')
    # cellformat = exce.add_format({'bg_color':'#123456','font_color':'#654321'})
    worksheet = exce.add_worksheet()

    # 从远端URL读取图片。
    url = 'https://raw.githubusercontent.com/jmcnamara/XlsxWriter/' + \
          'master/examples/logo.png'

    image_data = BytesIO(urlopen(url).read())

    # 向单元格写入字节流图片。注意，文件名必须显式指定。在这个例子中文件名会从URL字符串读取。
    worksheet.insert_image('B2', url, {'image_data': image_data})

    # 读取本地图片文件至字节流。注意，insert_image()方法可以直接这么干，此例只是为了演示。
    filename = './images/photo1.jpeg'

    image_file = open(filename, 'rb')
    image_data = BytesIO(image_file.read())
    image_file.close()

    # 将字节流图片写入单元格，文件名必须显式指定。
    worksheet.insert_image('B8', filename)
    worksheet.insert_image('B35',filename,{'image_data':image_data})
    worksheet.insert_image('Q16', filename,{'x_scale': 0.1, 'y_scale': 0.1})
    worksheet.insert_image('Q2', filename,{'x_scale': 0.5, 'y_scale': 0.5})
    worksheet.insert_image('Q19', filename,{'x_scale': 0.072, 'y_scale': 0.04})
    worksheet.insert_image(20,16, filename,{'x_scale': 0.072, 'y_scale': 0.04})

    # data = []
    # color = [''] * cols
    # cellcolor = ''
    # for i in range(rows):
    #     for j in range(cols):
    #         cellcolor = (hex(img[i,j,0])+hex(img[i,j,1])+hex(img[i,j,2])).replace('0x','')
    #         cellformat = exce.add_format({'bg_color': '#' + cellcolor,'font_color': '#' + cellcolor})

    # worksheet.conditional_format(get_xy(i,j),{'type':'cell','criteria':'<',\
    #                                           'value':50,'format':cellformat})
    exce.close()
main()