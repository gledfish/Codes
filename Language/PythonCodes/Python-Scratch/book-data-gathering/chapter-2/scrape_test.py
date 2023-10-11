from urllib.request import urlopen

html = urlopen("https://play.google.com/books/reader?id=VLqKMgAAAEAJ&pg=GBS.PA26.w.0.0.0.2_27")
print(html.read())

# urllib 文档

