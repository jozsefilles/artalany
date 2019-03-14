#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import requests
from lxml import etree

def download(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'}
    response = requests.get(url, headers=headers)
    return response.status_code, response.text

def crawl_page(url, xpath):
    status, html = download(url)
    tree = etree.HTML(html)
    result = tree.xpath(xpath)
    return result


if __name__ == '__main__':
    u = 'https://lumenet.hu/tungsram-sportlight-ultra-30-h7-4200k-58520sbu'
    x = 'number(translate((//*[@id="price_akcio_brutto_5994100002116"]/text())[3], ".", ""))'
    print(crawl_page(u, x))
