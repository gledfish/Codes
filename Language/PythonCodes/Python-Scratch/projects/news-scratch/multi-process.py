from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import threading

# 定义一个线程类
class MyThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        try:
            # 模拟浏览器打开网页
            html = urlopen(self.url)
            # 使用bs 对网页对象进行解析
            bsObj = BeautifulSoup(html, features="lxml")

            # 提取新闻标题和链接
            links = bsObj.findAll("a", href=re.compile("https://new.qq.com/rain/a/.*"))
            for link in links:
                link_text = link.get_text()
                link_url = link['href']
                print("链接文本内容：", link_text)
                print("链接内容：", link_url)
                print()

        except Exception as e:
            print("发生错误：", e)

# 创建多个线程并启动
urls = ["https://new.qq.com/", "https://www.baidu.com/", "https://www.google.com/"]
threads = []
for url in urls:
    thread = MyThread(url)
    thread.start()
    threads.append(thread)

# 等待所有线程完成
for thread in threads:
    thread.join()
