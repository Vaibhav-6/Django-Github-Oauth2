from django.shortcuts import render,HttpResponse
from bs4 import BeautifulSoup
import urllib
import requests
import json


# Create your views here.
def index(request):
    return render(request,'home.html')
def trending(request):
    lang=request.GET.get('lang','')
    url=f"https://github.com/trending/{lang}?since=daily"
    fetched_data=fetch_data(url)
    data=list(fetched_data)
    return render(request,'base.html',{'list': data})
def fetch_data(url):
    data=requests.get(url)
    soup= BeautifulSoup(data.text,'html.parser')
    data_article=soup.find_all('article',class_="Box-row")
    p_desc,href=[],[]
    dict_res={}
    for i in data_article:
        p_tag=i.find('p',class_="color-fg-muted")
        if p_tag!=None:
            p_desc.append(p_tag.get_text())
        heading=i.find('h1',class_='lh-condensed')
        href_data=heading.find('a', href=True)
        if href_data!=None:
            href.append(href_data['href'])
    # dict_res["Desc"]=p_desc
    # dict_res["Links"]=href
    mylist = zip(p_desc, href)
    #dict_res["range"]=range(len(href))
    return mylist 
    
  