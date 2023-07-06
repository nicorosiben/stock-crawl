import combination as cb
import tools as tl

request_list = {
    "beiz": "http://9.push2.eastmoney.com/api/qt/clist/get?cb=jQuery11240898109725081667_1688350619512&pn=1&pz=3000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:81+s:2048&fields=f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23&_=1688350622811",
    "shan": "http://9.push2.eastmoney.com/api/qt/clist/get?cb=jQuery11240898109725081667_1688350619516&pn=1&pz=3000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:1+t:2,m:1+t:23&fields=f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23&_=1688350619534",
    "shen": "http://9.push2.eastmoney.com/api/qt/clist/get?cb=jQuery11240898109725081667_1688350619516&pn=1&pz=3000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80&fields=f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23&_=1688350619521"}

def print_msg(str):
    if str == "shan":
        return "上证A股数据"
    elif str == "shen":
        return "深证A股数据"
    elif str == "beiz":
        return "北证A股数据"
    else:
        return "无数据链接"


for key_name, value in request_list.items():
    msg = f"正在获取{print_msg(key_name)}中，请稍后！"
    print(tl.color_font(msg,"green"))
    message = cb.get_info(value, key_name)
    print(message)
