from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
# 如果有属性，则尽量使用属性确定标签，让代码更加健壮
