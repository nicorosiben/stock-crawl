import requests

import tools as tool


def get_stock(url):
    resposne = requests.get(url)
    result_text = resposne.text
    result = tool.formate_stock(result_text)
    result = result['data']
    return result


def get_stock_total(stock_data):
    return stock_data['total']


def get_stock_diff(stock_data):
    return stock_data['diff']
