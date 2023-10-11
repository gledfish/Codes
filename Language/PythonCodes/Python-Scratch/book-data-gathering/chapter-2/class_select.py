from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())
# findAll  参数
# tag：一个或多个标签组成的列表
# attributes:属性:值组成的字典
# recursive：是否在子标签中寻找
# text:文本内容，用来与标签的内容进行匹配
# limit：获取前 limit 项结果
# keyword：选择具有指定属性的标签，（
allText = bsObj.findAll(id="text")
print(allText[0].get_text())