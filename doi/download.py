#onclick="location.href='https:\/\/sci.bban.top\/pdf\/10.1080\/02508060.2018.1516092.pdf?download=true'"
import os
import time
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

def search_article(artName):
    url = 'https://www.sci-hub.ren/'
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
               'Accept' : 'text/html,application/xhtml+xml, application/xml, q=0.9, image/webp, */*; q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Accept-Encoding':'gzip,deflate,br',
               "Content-Type":'application/x-www-form-urlencoded',
               'Content-Length':'123',
               'Origin':'https://www.sci-hub.ren/',
               'Connection':'close',
               'Upgrade-Insecure-Requests':'1'}
    data = {'sci-hub-plugin-check':'',
            'request':artName}
    res = requests.post(url,headers=headers,data=data,verify=False)
    html = res.text
    soup = BeautifulSoup(html,'html.parser')
    iframe = soup.find(id='pdf')
    if iframe == None:
        return ''
    else:
        downUrl = iframe['src']
        #downUrl = 'https:'+downUrl
        return downUrl
def download_article(downUrl):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml, q=0.9, image/webp, */*; q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Accept-Encoding': 'gzip,deflate,br',
               "Content-Type": 'application/x-www-form-urlencoded',
               'Content-Length': '123',
               'Origin': 'https://sci-hub.ren/',
               'Connection': 'close',
               'Upgrade-Insecure-Requests': '1'}
    res = requests.get(downUrl,headers=headers,verify=False)
    return res.content

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        print('---new folder...')
        os.makedirs(path)
    else:
        print('--文件已经存在！')
if __name__ =='__main__':
    # title = 'water'
    # mkdir(title)
    #
    # f=pd.read_csv('doi.csv',sep=',',header=None)
    # f_file = f.values.tolist()
    # num_no = 0
    # artic_num = len(f_file)
    #
    # for doi in f_file:
    #     request = str(doi[0])
    #     downUrl = search_article(request)
    #     if downUrl == '':
    #         num_no = num_no+1
    #         print('未下载/%s'%request)
    #         continue
    #     pdf = download_article(downUrl)
    #     with open('./'+title+'/%s.pdf'%request.replace('/','_'),'wb') as f:
    #         f.write(pdf)
    #     time.sleep(0.2)
    # print('下载完成，共下载:'+str(artic_num-num_no)+'/'+str(artic_num))

    DOI = '10.1080/02508060.2018.1516092'
    downUrl = search_article(DOI)
    print(downUrl)
    pdf = download_article(downUrl)
    with open('%s.pdf'%DOI.replace('/','_'),'wb') as f:
        f.write(pdf)
    time.sleep(0.2)
    print("下载完成！")
