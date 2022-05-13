"""
@File  : dytt_crawl.py
@Author: lyj
@Create  : 2022/5/12 16:59
@Modify  : 2022/5/12 16:59
@Desc  : 
"""
import json

import requests
from bs4 import BeautifulSoup

from flaskp.utils.web_utils import web_page_download
from flaskp.utils.xpath_utils import xpath_find


def get_film_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7',
        'Host': 'www.dytt8.net'}
    resp = requests.get(url, headers=headers)
    resp.encoding = 'gb2312'

    # html_doc = ''
    # with open('E:\\0_workspace\\python-workspace\\utils\\a.html', 'r') as f:
    #     html_doc = f.read()

    html_doc = resp.text
    soup = BeautifulSoup(html_doc, 'html.parser')

    content_div = soup.find('div', id='Zoom')
    img = content_div.find('img')
    cover = img.attrs['src']
    print(cover)
    a_link = content_div.find('a')
    magnet_link = a_link.attrs['href']
    print(magnet_link)
    # a_link.extract()

    content_data = content_div.text
    content_data = content_data.strip()
    with open('b.txt', 'w', encoding='utf-8') as f:
        f.write(content_data)
    content_list = content_data.split('\n')
    content_list = [x.strip() for x in content_list]
    content_data = ''.join(content_list)
    content_list = content_data.split('◎')
    for item in content_list:
        print(item)


def get_summary():
    xpath = "/html/body/div[@id='header']/div[@class='contain']/div[@class='bd2']/" \
            "div[@class='bd3']/div[@class='bd3r'][1]/div[1]/div[@class='bd3rl']/" \
            "div[@class='co_area2'][1]/div[@class='co_content8']/" \
            "ul/table/tr[{film_no}]/td[@class='inddline'][1]/a[2]"

    html_doc = web_page_download('https://dytt8.net/index2.htm', host='www.dytt8.net')

    data_list = []
    for i in range(2, 17):
        xpath_no = xpath.replace('{film_no}', '%d' % i)
        data = xpath_find(html_doc, xpath_no, ['href'])
        data_list.append(data)
    print(json.dumps(data_list, ensure_ascii=False))



if __name__ == '__main__':
    get_summary()
