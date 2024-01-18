from django.shortcuts import render

import requests
from bs4 import BeautifulSoup
from .models import Link
# Create your views here.
def home(request):
    urls=requests.get('https://www.google.com/')
    beautifulsoup=BeautifulSoup(urls.text,'html.parser')
    address=[]
    for link in beautifulsoup.find_all('a'):
        address=link.get('href')
        name=link.name
        Link.objects.create(name=name, address=address)
    data_values=Link.objects.all()
    return render(request,'home.html',{'data_values':data_values})