import requests
import urllib.request
import time
import os
from bs4 import BeautifulSoup


searchterm = testing

#url = 'https://polaris.hclibrary.org/polaris/search/'
url = 'https://polaris.hclibrary.org/polaris/search/searchresults.aspx?ctx=1.1033.0.0.3&type=Default&term=testing&by=KW&sort=MP&limit=TOM=*&query=&page=0&searchid=1'

response = requests.get(url)
html = response.text
print(response)

soup = BeautifulSoup(html, "html.parser")
soup.a


def getbooks():
    



#if onshelf == True:
#    print('Available -> ' + booktitle)

xpathonshelf = /html/body/div[2]/div/table/tbody/tr[11]/td[3]
