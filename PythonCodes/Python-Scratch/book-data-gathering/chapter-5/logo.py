from urllib.request import urlopen  
from bs4 import BeautifulSoup  
from urllib.request import urlretrieve  
  
html = urlopen("http://www.pythonscraping.com")  
bsObj = BeautifulSoup(html)  
  
logo_link = bsObj.find("a",{"id":"logo"})  
if logo_link is not None:  
    imageLocation = logo_link.find("img")["src"]  
    urlretrieve(imageLocation, "logo.icon")  
else:  
    print("Logo link not found")