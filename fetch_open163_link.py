#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
@author: zfr
@file: spider_example_requests_beautifulsoup.py
"""

import requests
from bs4 import BeautifulSoup
from lxml import etree
import re

def fetch_open163_link(online = True, debug = False):
    if online:
        html_content = ""
        # 可以在多次访问中保留cookie
        s = requests.Session()
        headers = {}
        headers[
            'User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F'
        headers['Referer'] = 'http://open.163.com/'
        if debug:
            print(headers)
        url = 'http://open.163.com/special/financialmarkets/'
        url = 'http://open.163.com/special/economics/'
        url = 'http://open.163.com/special/Khan/macroeconomics.html'
        url = 'http://open.163.com/special/opencourse/financialtheory.html'
        r = s.get(url, headers=headers, timeout=10, allow_redirects=True)
        if debug:
            r.raise_for_status()
        r.encoding='gb18030'
        html_content = r.content
        soup = BeautifulSoup(html_content,'html.parser', from_encoding='gb18030')
        print('# ' + soup.title.text)
        pass
    else:
        path='Z:\\kh.html'
        htmlfile = open(path, 'r', encoding='utf-8')
        soup = BeautifulSoup(htmlfile.read(),'html.parser')
        pass

    try:
        # find() 返回的是单个soup对象
        #fetch_item = soup.find(name='div', attrs={'class': 'main_center_news'})
        # find_all() 返回的是由多个soup对象组成的list
        #fetch_item = fetch_item.find_all('div',attrs={'class': re.compile(r'^mod_.*news\d*$')})
        #fetch_item = soup.find_all('div',attrs={'class': re.compile(r'^mod_.*news\d*$')})
#        print(soup.h)
        n=0
        fetch_item = soup.find_all('table',attrs={'id': 'list2'})
        for a in fetch_item:
            b_list = a.find_all('td',attrs={'class': 'u-ctitle'})
            for b in b_list:
#                print(b)
                c_list = b.find_all('a')
                for c in c_list:
#                    print('#################')
#                    print(c)
                    n+=1
#                    print(str(n) + ": " + c.text.strip().replace(' ','_').replace('(','').replace(')',''))
                    print("you-get  " + c['href'] + " -O " + str(n).zfill(3) + "_" + c.text.strip().replace(' ','_').replace('(','').replace(')',''))
#                    print(c['href'])
    except:
        raise
        pass

if __name__ == '__main__':
    fetch_open163_link(online = True, debug = False)
    print('OK')
