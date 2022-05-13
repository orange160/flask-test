"""
@File  : web_utils.py
@Author: lyj
@Create  : 2022/5/13 10:47
@Modify  : 2022/5/13 10:47
@Desc  : web页面的工具类
"""
import requests


def web_page_download(url, host='', encoding='gb2312'):
    """
    获取web的页面
    :param url: 页面连接
    :param host: 页面的host
    :param encoding: 编码，中文网站默认为gb2312，否则中文为乱码
    :return: 获取的html字符串
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7',
        'Host': host}
    resp = requests.get(url, headers=headers)
    resp.encoding = encoding
    return resp.text
