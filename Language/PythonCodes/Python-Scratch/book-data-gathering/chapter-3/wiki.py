from urllib.request import urlopen
from bs4 import BeautifulSoup
import re 
import datetime
import random

# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html)
# for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):

#     if 'href' in link.attrs:
#         print(link.attrs['href'])

random.seed()

def getLinks(articleUrl):
    # 获得一个 网页中所有指向其他词条的url
    html = urlopen("http://en.wikipedia.org" + articleUrl) 
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
# 循环获得 url
while len(links) > 0:
    newArticle = links[random.randint(0,len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)

