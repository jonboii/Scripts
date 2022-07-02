import requests
import urllib.request
import time
import os
from bs4 import BeautifulSoup
import selenium

#TODO: pull from csv/word/make list to integrate for search terms
#TODO: 



#url = "https://polaris.hclibrary.org/polaris/search/searchresults.aspx?ctx=1.1033.0.0.3&type=Default&term=findme&by=KW&sort=MP&limit=TOM=*&query=&page=0&searchid=1"
###########################Starting bs4 trial#############################
#response = str(requests.get(url))
#This will check to see if the url is available by getting the correct 200 response from the web server
#if response[11:14].string == '200':
#    result = requests.get(url)
#    print(result.text)
#result = requests.get(url)
#doc = BeautifulSoup(result.text, "html.parser")
#tag = doc.find_all(["span"], text="findme")
#print(tag)
#if onshelf == True:
#    print('Available -> ' + booktitle)
###xpathonshelf = /html/body/div[2]/div/table/tbody/tr[11]/td[3]###
###resrouces:
#https://www.youtube.com/watch?v=gRLHr664tXA
#https://www.youtube.com/watch?v=lOzyQgv71_4


############################Starting selenium trial#############################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
#import from a file for search terms (csv, or txt)
bookfile = 'A:\Jonathan\Documents\Scripts\resources\book_listing.xlsx'
#for loop to iterate over each search term
for book in bookfile:
    book = searchterm
#if statment to see if it's a book
images = driver.find
mediatype = images.find
if mediatype == book:
#ck to see availability (limiting to that branch)
branches = driver.find_element()
elkbranch = branches.find_by_elements()\
onshelf = elkbranch.find
if str(onshelf) == on shelf:
    print(searchterm + " is Available!")
else:
    print(searchterm + " is not there =(")


searchterm = "victory Matsui"
#preparing to be put into URL
searchterm.replace(' ', '%20')

url = "https://polaris.hclibrary.org/polaris/search/searchresults.aspx?ctx=1.1033.0.0.3&type=Keyword&term=" + searchterm + "&by=KW&sort=MP&limit=TOM=*&query=&page=0&searchid=1"

#path to chrome driver
PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get(url)
print(driver.title)





#Best to worst(id, name, class)

#This will be helpful for when I need to find availability
#search = driver.find_element_by_id("textboxTerm")
#search.send_keys("victory")
#search.send_keys(Keys.RETURN)
#driver.find_elements_by_class_name
#try:
#    content = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.ID, "searchResultsDIV"))
#    )
#    #print(content.text)
#    titles = content.find_elements_by_class_name("nsm-brief-primary-title-group")
#    title = titles.find_element_by_class_name("nsm-short-item nsm-e135")
#    print(title.text)
#except:
#    driver.quit()
#
#print(search)
