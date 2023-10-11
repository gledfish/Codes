from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
'''
爬取博客园首页所有的文章标题和链接，并保存在文件中。
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}



def getNews(url):
    try:
         # 模拟浏览器打开网页
        req = Request(url, headers=headers)
        html = urlopen(req)
        # 使用bs 对网页对象进行解析
        bsObj = BeautifulSoup(html, features="lxml")
        
        # 提取新闻标题和链接
        divs = bsObj.findAll("div", class_ = "post-item-text")
        print(len(divs))

        with open("articles.txt", "w", encoding="utf-8") as file:
            for div in divs:
                link = div.find("a")
                link_text = link.get_text()
                link_url = link['href']
                file.write("链接文本内容：" + link_text + "\n")
                file.write("链接内容：" + link_url + "\n\n")
                print("链接文本内容：", link_text)
                print("链接内容：", link_url)
                print()

    except Exception as e:
        print("发生错误：", e)

if __name__ == "__main__":
    getNews("https://www.cnblogs.com/")


## 实测可以爬取博客园，但是不能爬取腾讯新闻
