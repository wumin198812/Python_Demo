import json
import requests
from lxml import etree
import ip_proxies
proxies1=ip_proxies
print(proxies1)
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
# url="https://haokan.baidu.com/videoui/page/search?pn=2&rn=10&_format=json&tab=video&query=python"
# res=requests.get(url,headers=headers)
# data=json.loads(res.text)
# lists=data['data']['response']['list']
# for list in lists:
# #     print(list['title'],list['url'])
#     url1=list['url']
#     video_title=list['title']+ '.mp4'
#     print(url1)
#     video_html=requests.get(url1,headers=headers)
#     data1=etree.HTML(video_html.text)
#     video_url=data1.xpath('//video/@src')
#     for i in video_url:
#         video_data=requests.get(i,headers=headers,timeout=3).content
# #         video_datas=video_data.content
#         print (i)
#         with open(video_title,'wb') as f:
#             f.write(video_data)
#             print("下载完成")