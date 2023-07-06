import os
import progressbar
import time
from datetime import date

from openpyxl import Workbook

import get_data as dg
import tools as tool

# 创建股票信息数组
stock_list = []
# 临时存储股票分红融资数据
stock_red_dict = {}


def get_info(list_url, filename):
    data = dg.get_stock(list_url)
    quantity = len(data['diff'])
    info = dg.get_stock_diff(data)
    bar = progressbar.ProgressBar(max_value=quantity)
    print(f"========================================当前股票总数：{quantity}==========================================")
    print("读取股票数据中，请稍后。。。。。。")
    for i in range(quantity):
        number = i + 1
        new_price = info[i]['f2']
        quote_change = info[i]['f3']
        change_amount = info[i]['f4']
        turnover_hand = info[i]['f5']
        turnover_hand = tool.formate_number(turnover_hand)
        turnover_price = info[i]['f6']
        turnover_price = tool.formate_number(turnover_price)
        amplitude = info[i]['f7']
        turnover_rate = info[i]['f8']
        pe_ratio = info[i]['f9']
        volume_ratio = info[i]['f10']
        stock_number = info[i]['f12']
        exchange = tool.convert_number(stock_number)
        stock_name = info[i]['f14']
        max_price = info[i]['f15']
        low_price = info[i]['f16']
        today_price = info[i]['f17']
        yesterday_price = info[i]['f18']
        total_price = info[i]['f20']
        total_price = tool.formate_number(total_price)
        circulate_price = info[i]['f21']
        circulate_price = tool.formate_number(circulate_price)
        price_tobook = info[i]['f23']
        stock_dict = {
            'number': number,
            'new_price': new_price,
            'quote_change': quote_change,
            'change_amount': change_amount,
            'turnover_hand': turnover_hand,
            'turnover_price': turnover_price,
            'amplitude': amplitude,
            'turnover_rate': turnover_rate,
            'pe_ratio': pe_ratio,
            'volume_ratio': volume_ratio,
            'stock_number': stock_number,
            'exchange': exchange,
            'stock_name': stock_name,
            'max_price': max_price,
            'low_price': low_price,
            'today_price': today_price,
            'yesterday_price': yesterday_price,
            'total_price': total_price,
            'circulate_price': circulate_price,
            'price_tobook': price_tobook
        }
        stock_list.append(stock_dict)
        time.sleep(0.0001)
        bar.update(number)
    bar.finish()
    message = write_in_excel(stock_list, filename)
    return message

def write_in_excel(gupiao_list, filename):
    try:
        get_date = date.today()
        if os.path.exists(f'{filename}_{get_date}.xlsx'):
            os.remove(f'{filename}_{get_date}.xlsx')
        workbook = Workbook()
        sheet = workbook.active
        sheet.append([
            '编号',
            '最新价',
            '涨跌幅',
            '涨跌额（元）',
            '成交量（手）',
            '成交额',
            '振幅',
            '换手率',
            '市盈率',
            '量比',
            '股票代码',
            '交易所',
            '股票名称',
            '最高',
            '最低',
            '今开',
            '昨收',
            '总市值',
            '流通市值',
            '市净率'
        ])
        for item in gupiao_list:
            sheet.append([
                item['number'],
                item['new_price'],
                str(item['quote_change']) + "%",
                item['change_amount'],
                item['turnover_hand'],
                item['turnover_price'],
                str(item['amplitude']) + "%",
                str(item['turnover_rate']) + "%",
                item['pe_ratio'],
                item['volume_ratio'],
                item['stock_number'],
                item['exchange'],
                item['stock_name'],
                item['max_price'],
                item['low_price'],
                item['today_price'],
                item['yesterday_price'],
                item['total_price'],
                item['circulate_price'],
                item['price_tobook']
            ])
        workbook.save(f'{filename}_{get_date}.xlsx')
        return tool.color_font("数据写入文件成功","green")
    except Exception as e:
        print(e)
        return tool.color_font("数据写入文件失败","red")
