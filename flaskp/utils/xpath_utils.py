"""
@File  : xpath_crawl.py
@Author: lyj
@Create  : 2022/5/13 10:07
@Modify  : 2022/5/13 10:07
@Desc  : 
"""
from lxml import etree


def element_to_string(ele):
    """
    将lxml的element转换为字符转
    :param ele:
    :return:
    """
    s = etree.tostring(ele, encoding='utf-8').strip().decode('utf-8')
    # 正则替换HTML标签， 保留内容， 非贪婪模式
    # return re.sub('<[^>]*>', '', s).strip()
    return s


def xpath_find(html_doc, xpath, attrs):
    """
    通过xpath获取html_dock中的元素的text和属性值
    :param html_doc: html
    :param xpath: xpath路径
    :param attrs: 指定元素的属性，元组或者列表
    :return: 字典值
    """
    tree = etree.HTML(html_doc)
    found_list = tree.xpath(xpath)
    ret_list = []
    for d in found_list:
        found_dict = {'text': d.text}
        for attr in attrs:
            found_dict[attr] = d.attrib[attr]
        ret_list.append(found_dict)
    return ret_list



