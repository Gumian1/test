# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 20:43:19 2022

@author: Zhanghao
"""

import time
import os
from lxml import etree
import requests
import random
from selenium import webdriver
num = 0
def main():
    global num
    body = webdriver.Chrome()
    body.get("https://www.emol.com/buscador/?query=china")
    response = body.page_source    #获取网页源码
    html_str = etree.HTML(response)   #HTML格式展示
    urls = html_str.xpath(r'//div[@class="cont_bus_txt_detall"]/a/@href')
    print(urls)
    for i in range(1, 7):
        print('获取第' + str(i) + "页")
        for url in urls[1:]:
            time.sleep(1)
            html = request(url)
            num += 1
            print("正在爬取第" + str(num) + "个：" + url)
            content(html)
        button=body.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/div/nav[2]/ul/li[2]/a/span')
        button.click()
        response = body.page_source    #获取网页源码
        html_str = etree.HTML(response)    #HTML格式展示
        urls = html_str.xpath(r'//div[@class="cont_bus_txt_detall"]/a/@href')


#保存新闻
def save(title,text,time):

    # 判断数据存储文件是否存在
    file = "./智利.csv"
    if os.path.exists(file):
        sz = os.path.getsize(file)
        if not sz:
            with open(file, "a", encoding="utf-8") as f:
                f.write("日期,标题,文本\n")
    else:
        with open(file, "a", encoding="utf-8") as f:
            f.write("日期,标题,文本\n")
    with open(file, "a", encoding="utf-8") as f:
        f.write('"'+time+'","'+title+'","'+text+'"\n')



#使用requests模块获取新闻内容
def request(url):
    useragents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        'User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
        'User-Agent:Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
        'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',
        'User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)',
        'User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)',
        'User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'User-Agent:Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
        'User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12',
        'User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
        'User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
        'User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
        'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201',
        'User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201',
    ]

    # 设置随机UA

    userA = random.choice(useragents)
    heards = {
              'User-Agent': userA,
             }

    # requests模块访网设置代理若需代理请添加代理ip
    proix = {}

    while True:
        try:
            response = requests.get(url=url, headers=heards, proxies=proix, timeout=30)
            break
        except:
            print("获取url失败正在重新获取")
            return 0
    html = response.text
    html = etree.HTML(html)
    return html
def content(html):
    # 获取新闻标题
    try:
        title = html.xpath("//h1//text()")[0]
        print(title)
    except:
        title=''
    # 获取新闻内容
    try:
        texts = html.xpath("/html/body/div[5]/div[2]/div/div[1]/div/div[1]//div/text()")
        text = ""
        for i in texts:
            text = text + i.xpath('string(.)').replace('\n', ' ').replace(',', '，').replace("'", "‘").replace('"', "”").replace("\r", " ").replace(" ", " ")
    except:
        text=''
    # 获取新闻日期
    #try:
    time=html.xpath("/html/body/div[5]/div[1]/div[2]/div[1]/text()")
    print(time)
    time_1=''
    for i in time:
        time_1+=i
    time_1=time_1.replace(' ','').replace('\n','').replace('-','')
    print(time_1)
    if time_1 != '':    
        save(title,text,time_1)
if __name__ == '__main__':
    main()