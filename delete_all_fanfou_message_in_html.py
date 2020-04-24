#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
@filename: delete_all_fanfou_message_in_html.py
@author: No Name
@date: 2020-04-23
"""

import sys
import time

def test_firefox(url_delete):
    from selenium import webdriver
    driver = webdriver.Firefox(firefox_binary='D:\\app\\brower_driver\\Mozilla Firefox\\firefox.exe',
                              executable_path='D:\\app\\brower_driver\\geckodriver.exe')
    driver.get('https://fanfou.com/')
    driver.find_element_by_id('loginname').send_keys('你的账号')
    driver.find_element_by_id('loginpass').send_keys('你的密码')
    time.sleep(1)
    driver.find_element_by_class_name('formbutton').click()
    time.sleep(2)
    for item in url_delete:
        try:
            print(item)
            driver.get(item)
            driver.find_element_by_class_name('formbutton').click()
            time.sleep(0.3)
        except:
            pass
    print(driver.current_url)
    time.sleep(3)
    driver.quit()

def get_all_html():
    import os
    all_html_file = []
    for parent,dirnames,filenames in os.walk('Z:\\fanfou_html'):
        for filename in filenames:
            all_html_file.append(os.path.join(parent,filename))
    return all_html_file

def parse_url(all_html_file):
    from bs4 import BeautifulSoup
    from lxml import html
    all_html_link = []
    for f_html in all_html_file:
        with open(f_html, mode = 'r', encoding='utf-8') as f:
            html_content = f.read()
        soup = BeautifulSoup(html_content,'html.parser')
        try:
            fetch_item = soup.find_all('a', attrs={'class': 'post_act delete'})
            for item in fetch_item:
                all_html_link.append('https://fanfou.com' + item['href'])
        except:
            pass
    return all_html_link

if __name__ == '__main__':
    all_html_file = get_all_html()
    # print(all_html_file)
    all_html_link = parse_url(all_html_file)
    # print(all_html_link)
    print(len(all_html_link))
    test_firefox(all_html_link)

