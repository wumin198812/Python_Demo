import requests
import json
from lxml import etree
from bs4 import BeautifulSoup
import ip_proxies
myproxy=ip_proxies.proxies
# print(myproxy)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
def get_url(base_url):#
    ress=[]
    for i in range(1,3):
        url=base_url+str(i)+'.html'
        res=requests.get(url,proxies=myproxy,headers=headers).text
        index_html=etree.HTML(res)
        story_urls=index_html.xpath('//div[@class="list_article"]/ul/li/a/@href')
        for story_url in story_urls:
            ress.append('http://chunchao.xyz'+story_url)
    return ress
def get_story(ress_url):
    res=requests.get(ress_url,headers=headers,proxies=myproxy).content
#     index_html=etree.HTML(res)
    soup=BeautifulSoup(res, 'html.parser')
#     text1=index_html.xpath('//book/p//text()')
    text1=soup.find_all('book')
    print(text1)
    for text in text1:
        print(text)
#     return text
if __name__ == '__main__':
    base_url='http://chunchao.xyz/?s=book/type/26/'
    ress=get_url(base_url)
    for ress_url in ress:
        print(ress_url,'\n')
        html=requests.get(ress_url,headers=headers,proxies=myproxy).text
        soup=BeautifulSoup(html, 'html.parser')
        texts=soup.find_all("book")
        print(texts)
#         index_html=etree.HTML(html)
#         texts=index_html.xpath('//book/p/text()')
        for text in texts:
            print(text)
            with open ('2.txt','wb') as f :
                f.write(text)
        print("写入完成")
#         text=get_story(ress_url)
#         with open ('','a') as f:
#                 f.write()