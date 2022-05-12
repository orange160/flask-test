"""
@File  : dytt_crawl.py
@Author: lyj
@Create  : 2022/5/12 16:59
@Modify  : 2022/5/12 16:59
@Desc  : 
"""


import requests
from bs4 import BeautifulSoup


def get_film_info(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
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


if __name__ == '__main__':
    # url = 'https://www.dytt8.net/html/gndy/dyzz/20220509/62587.html'
    # url = 'https://www.dytt8.net/html/gndy/dyzz/20220506/62582.html'
    # url = 'https://www.dytt8.net/html/gndy/dyzz/20220505/62578.html'
    url = 'https://www.dytt8.net/html/gndy/dyzz/20220418/62530.html'
    get_film_info(url)