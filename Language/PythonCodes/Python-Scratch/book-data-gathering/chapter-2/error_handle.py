from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    # 尝试打开网址
    try:
        html = urlopen(url)
    # 打开失败，抛出错误
    except HTTPError as e:
        return None
    # 打开成功，但没有想要的字段，抛出错误
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None 
    return title
title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("title could not be found")
else:
    print(title)
    