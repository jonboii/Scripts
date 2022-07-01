import requests
import urllib.request
import time
import os
from bs4 import BeautifulSoup
#TODO: pull from csv/word/make list to integrate for search terms
#TODO: 




url = 'https://polaris.hclibrary.org/polaris/search/searchresults.aspx?ctx=1.1033.0.0.3&type=Default&term=hello&by=KW&sort=MP&limit=TOM=*&query=&page=0&searchid=1'


response = str(requests.get(url))

#This will check to see if the url is available by getting the correct 200 response from the web server
#if response[11:14].string == '200':
#    result = requests.get(url)
#    print(result.text)


result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
title = doc.find_all('testing')
print(title)




#if onshelf == True:
#    print('Available -> ' + booktitle)

###xpathonshelf = /html/body/div[2]/div/table/tbody/tr[11]/td[3]###
