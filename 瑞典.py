import random
import os
from lxml import etree
import requests
num = 0
def main():
    global num
    body = request('https://admin.openxlab.org.cn/admin/datasets/upload?isHot=true&pageNo=1&pageSize=10')
    urls = body.xpath("//div")

    print(urls)
    for url in urls:
        print(url.text)
        file = "./热门.csv"
        if os.path.exists(file):
            sz = os.path.getsize(file)
            if not sz:
                with open(file, "a", encoding="utf-8") as f:
                    f.write("热门数据集\n")
        else:
            with open(file, "a", encoding="utf-8") as f:
                f.write("热门数据集\n")
        with open(file, "a", encoding="utf-8") as f:
            f.write('"' + str(url) + '","')

#保存新闻
def save(title,text,time):
    # 判断数据存储文件是否存在
    file = "./瑞典.csv"
    if os.path.exists(file):
        sz = os.path.getsize(file)
        if not sz:
            with open(file, "a", encoding="utf-8") as f:
                f.write("日期,标题,文本\n")
    else:
        with open(file, "a", encoding="utf-8") as f:
            f.write("日期,标题,文本\n")
    with open(file, "a", encoding="utf-8") as f:
        f.write('"'+str(time[0])+'","'+str(title)+'","'+str(text)+'"\n')

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
    userA = random.choice(useragents)
    # 设置随机UA
    heards = {
              'User-Agent': userA,
            'cookies':'uaa-token=eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiIxNjc0MDEiLCJyb2wiOiJST0xFX1JFR0lTVEVSLFJPTEVfREFUQVNFVCIsImlzcyI6Ik9wZW5YTGFiIiwiaWF0IjoxNzA0ODgxODI2LCJwaG9uZSI6IjE1MTM1NDc2NzEyIiwiZW1haWwiOiIyMzY4NTEzMzE3QHFxLmNvbSIsImV4cCI6MTcwNTQ4NjYyNn0.gg14wWmb3qlRzqSnsNLMWO_hUZGZu-n7Q3qhbqN2UA0plHNiHrcAsQPEkvmDYllBmTAFGk31pNJjepOvUEyubA; ssouid=167401; _ga=GA1.1.640077080.1704882388; _ga_WBG70LP3Q4=GS1.1.1704882387.1.0.1704882391.0.0.0; _ga_MVGXEQWG6Y=GS1.1.1704882393.1.1.1704882403.0.0.0; opendatalab_session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjMxOTAzLCJOYW1lIjoieWlrZXNodSIsIkVtYWlsIjoiMjM2ODUxMzMxN0BxcS5jb20iLCJQaG9uZSI6IjE1MTM1NDc2NzEyIiwiR2l0SHViQWNjb3VudCI6IiIsIldlQ2hhdEFjY291bnQiOm51bGwsIlpoaWh1QWNjb3VudCI6bnVsbCwiT3JnYW5pemF0aW9uIjpudWxsLCJFeHBpcnkiOiIyMDI0LTA0LTA5VDE4OjQ2OjA1LjU0MDkxOTk0OCswODowMCIsIlJvbGUiOiIiLCJJc0ludGVybmFsIjp0cnVlLCJTc29VaWQiOiIxNjc0MDEiLCJBdmF0YXIiOm51bGwsIk5pY2tuYW1lIjoieWlrZXNodSJ9.dvihCalpksjpzUsgXoETOFuaFgdnPHlZTHuZnaB5f6g; _ga_T1XBX31PXD=GS1.1.1704883572.1.0.1704883576.0.0.0; _ga_N30YTBKM5S=GS1.1.1704883577.1.0.1704883580.0.0.0; _ga_7Q4NTYQ4VQ=GS1.1.1704883582.1.0.1704883585.0.0.0; _ga_C63C2X4TB3=GS1.1.1704883564.1.1.1704883586.0.0.0; acw_tc=260980f1-10af-42da-bada-47957751dcd35915ad94086cf781548932caf06e6bbd'
             }
    
    # requests模块访网设置代理若需代理请添加代理ip
    proix = {}

    while True:
        try:
            response = requests.get(url=url, headers=heards, proxies=proix, timeout=30)
            print(response)
            break
        except:
            print("获取url失败正在重新获取")
            return 0
    html = response.content
    html = etree.HTML(html)
    return html
# def content(html):
#     # 获取新闻标题
#     title = html.xpath("//h1")[0].text.replace('\n', ' ').replace(',', '，').replace("'", "‘").replace('"', "”").replace("\r", " ").replace(" ", " ")
#     print(title)
#     # 获取新闻内容
#     texts = html.xpath("//div[@class='Body']/p")
#     text = ""
#     for i in texts:
#         text = text + i.xpath('string(.)').replace('\n', ' ').replace(',', '，').replace("'", "‘").replace('"', "”").replace("\r", " ").replace(" ", " ")
#     # 获取新闻日期
#     time = html.xpath("//div[@class='Meta-part Meta-part--published']/time/text()")
#     print(time)
#     a=[]
#     a[0]
#     save(title,text,time)


if __name__ == '__main__':
    main()