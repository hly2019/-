# -*- coding = utf-8 -*-
# @Time : 2020/9/9 11:57
# @Author : hly
# @File : crawler_mtime.py
# @Software : PyCharm
import os
import sys
from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import xlwt
import _sqlite3
import urllib
import json
find_movie = re.compile(r'href="(.*?)"')
# find_jianjie = re.compile(u"[\u4E00-\u9fA5A-Z\\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\·]+")
find_jianjie = re.compile(u"[\u4E00-\u9fA5\a-zA-Z\s\t\u3000\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\·]+")
find_title = re.compile(u"[\u4E00-\u9fA5]+")
find_actor_html = re.compile(r'href="(.*?)"')
find_actor_name = re.compile(u"[\u4E00-\u9fA5\·]+[\u4E00-\u9fA5]")
find_actor_pic = re.compile(r'src="(.*?)"')
find_actor_info = re.compile(u"[\u4E00-\u9fA5\a-zA-Z\s\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\·]+")
find_prize = re.compile(u"[0-9]+")
num = 0



#返回url对应的html
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    #伪装成浏览器
    request = urllib.request.Request(url, headers= head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        html = html.replace("\\","")
        # print(html)
    except urllib.error.URLError as e :
        if hasattr(e,"code"):
            print(e.code)
        if(hasattr(e,"reason")):
            print(e.reason)
    return html

#从html页面爬取上面的电影的url
def get_movie(html):
    soup = BeautifulSoup(html, "html.parser")
    list_ = []
    # print(html)
    for item in soup.find_all('div', class_="td pl12 pr20"):
        item = str(item)
        # print(item)
        link = re.findall(find_movie, item)[0]#每部电影的url
        # print(link)
        html1 = askURL(link)#获取每部电影的html















if __name__ == "__main__":
    html = askURL("http://service.channel.mtime.com/service/search.mcs?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Channel.Pages.SearchService&Ajax_CallBackMethod=SearchMovieByCategory&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2Fmovie%2Fsearch%2Fsection%2F%23sortType%3D4%26viewType%3D0%26pageIndex%3D1%26rating%3D2_10&t=20209812434290816&Ajax_CallBackArgument0=&Ajax_CallBackArgument1=0&Ajax_CallBackArgument2=0&Ajax_CallBackArgument3=0&Ajax_CallBackArgument4=0&Ajax_CallBackArgument5=0&Ajax_CallBackArgument6=0&Ajax_CallBackArgument7=0&Ajax_CallBackArgument8=&Ajax_CallBackArgument9=0&Ajax_CallBackArgument10=0&Ajax_CallBackArgument11=2&Ajax_CallBackArgument12=10&Ajax_CallBackArgument13=0&Ajax_CallBackArgument14=1&Ajax_CallBackArgument15=0&Ajax_CallBackArgument16=1&Ajax_CallBackArgument17=4&Ajax_CallBackArgument19=0&Ajax_CallBackArgument18=1")
    get_movie(html)