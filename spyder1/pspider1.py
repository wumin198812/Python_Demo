import requests
from lxml import etree
from bs4 import BeautifulSoup
myheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
myproxy={'https':'27.184.146.96:8118'}
for i in range(1,3):
    url5='http://www.meinvtu.site/list-cateId-2.html?page='
    url6=url5+str(i)
    index=requests.get(url6,headers=myheader,proxies=myproxy)
    print(index.status_code)
    html=etree.HTML(index.content)
    url_list=html.xpath('//a[@class="item-wrap"]/@href')
    print (url_list)
    for myurl in url_list:
#         print (myurl)
        re=requests.get(myurl,headers=myheader,proxies=myproxy)
        html_data=etree.HTML(re.content)
        # print(html_data)
        img_list = html_data.xpath('//img[@class="img-lazy"]/@data-original')
        print(img_list)