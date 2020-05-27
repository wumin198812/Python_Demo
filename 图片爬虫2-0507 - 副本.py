#!/usr/bin/env python
# coding: utf-8

# In[19]:


import requests
from lxml import etree 
from bs4 import BeautifulSoup
myheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
myproxy={'https':'27.184.146.96:8118'}
url5='http://www.meinvtu.site/list-cateId-2.html?page=1'
index=requests.get(url5,headers=myheader,timeout=2,proxies=myproxy)
print(index.status_code)
html=etree.HTML(index.content)
myurls=html.xpath('//a[@class="item-wrap"]/@href')
print(myurls)


# In[ ]:




