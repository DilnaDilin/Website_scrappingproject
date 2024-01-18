from django.shortcuts import render

import requests
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
    urls=requests.get('https://www.google.com/')
    beautifulsoup=BeautifulSoup(urls.text,'html.parser')
    address=[]
    for link in beautifulsoup.find_all('a'):
        address.append(link.get('href'))
        #name=link.name
    return render(request,'home.html',{'address':address})