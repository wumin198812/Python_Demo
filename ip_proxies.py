#!/usr/bin/env python
# coding: utf-8

# In[29]:


# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用
 
from bs4 import BeautifulSoup
import requests
import random
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
# myproxy={'https':'27.184.146.96:8118'}
def getHTMLText(url,proxies):
    try:
        r = requests.get(url,proxies=myproxy)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        return 0
    else:
        return r.text
def get_ip_list(url):
    web_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(web_data.text, 'html')
    ips = soup.find_all('tr')
#     print(ips)
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[5].text+ '://' + tds[1].text + ':' + tds[2].text)
# 检测ip可用性，移除不可用ip：（这里其实总会出问题，你移除的ip可能只是暂时不能用，剩下的ip使用一次后可能之后也未必能用）
    for ip in ip_list:
        try:
          res = requests.get(url1,proxies=ip,headers=headers,timeout=1)
        except Exception as e:
          ip_list.remove(ip)
          continue
    return ip_list
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append(ip)
    proxy_ip = random.choice(proxy_list)
    print(proxy_ip)
    proxies = {proxy_ip}
    return proxies
if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    for i in range(1,5):
        urls=url+str(i)
        ip_list = get_ip_list(urls)
        print('IP列表：',ip_list)
    proxies = get_random_ip(ip_list)
    print(proxies)


# In[ ]:




