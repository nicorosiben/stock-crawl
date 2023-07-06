import json
import re
from datetime import datetime


def formate_stock(text):
    formate_json = text[text.index('(') + 1:-2]
    formate_text = json.loads(formate_json)
    return formate_text


def formate_number(number):
    if re.match(r'^\d+(\.\d+)?$', str(number)):
        if len(str(number).split('.')[0]) >= 9:
            number = '{:.2f}亿'.format(float(number) / 100000000)
        else:
            number = '{:.2f}万'.format(float(number) / 10000)
    else:
        number = 00000
    return number


def convert_number(number):
    if str(number).startswith(('600', '601', '603', '605')):
        return '上证主板A股'
    elif str(number).startswith(('688', '689')):
        return '科创板（上证）'
    elif str(number).startswith(('000', '002', '003', '001')):
        return '深圳主板A股'
    elif str(number).startswith(('300', '301')):
        return '创业板（深证）'
    elif str(number).startswith(('43', '83', '87')):
        return '北证主板A股'
    else:
        return 'Unknown'


def color_font(str, color):
    color_code = get_color_code(color)
    return f"{color_code}{str}\033[0m"


def get_color_code(color_name):
    color_codes = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }
    return color_codes.get(color_name, '')


def classify_number(number):
    if str(number).startswith('60'):
        return "sh"
    elif str(number).startswith('68'):
        return "sh"
    elif str(number).startswith('00'):
        return "sz"
    elif str(number).startswith('30'):
        return "sz"
    elif str(number).startswith(('43', '83', '87')):
        return "bj"
    else:
        return "NN"


def get_year():
    now = datetime.now()
    year = now.year
    return year


def get_month():
    now = datetime.now()
    month = now.month
    return month


def get_day():
    now = datetime.now()
    day = now.day
    return day


def formate_date_yyyy_mmm_dd(date_str):
    if date_str == "-----" or date_str is None:
        return date_str
    else:
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            return "日期格式无效"


def round_to_5_decimal_places(number, decimal=5):
    try:
        rounded_number = round(number, decimal)
        return rounded_number
    except Exception as e:
        print(e)
        return 0.00000


def str_to_int(str_value, num):
    try:
        int_value = int(str_value)
        return int_value
    except ValueError:
        print(color_font("输入格式不正确，将使用默认数值！可关闭程序重新运行。。。。。。", "red"))
        return num
