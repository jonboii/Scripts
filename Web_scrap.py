import selenium
from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get('http://lodging.net')
find = driver.find_element_by_xpath
find2 = driver.find_elements_by_link_text
wait = driver.implicitly_wait('30')
startdate = 'MM/DD/YYYY'
enddate = 'MM/DD/YYYY'


find('/html/body/form/div[5]/div[2]/div/div[1]/div/div[7]/span/input').click()

#to get get around trusting the website
wait
find('/html/body/div/div[2]/button[3]').click()
find('/html/body/div/div[3]/p[2]/a').click()

#dates
find('/html/body/table/tbody/tr[1]/td[2]/div[1]/div[2]/form/div/table/tbody/tr[1]/td[1]/div/table[1]/tbody/tr[2]/td[1]/input').send_keys(startdate)
find('/html/body/table/tbody/tr[1]/td[2]/div[1]/div[2]/form/div/table/tbody/tr[1]/td[1]/div/table[1]/tbody/tr[2]/td[2]/input').send_keys(enddate)

#selection of E5
find('/html/body/table/tbody/tr[1]/td[2]/div[1]/div[2]/form/div/table/tbody/tr[1]/td[1]/div/table[3]/tbody/tr[2]/td[3]/select').click()
find('/html/body/table/tbody/tr[1]/td[2]/div[1]/div[2]/form/div/table/tbody/tr[1]/td[1]/div/table[3]/tbody/tr[2]/td[3]/select/option[6]').click()

#selection of TDY
find('/html/body/table/tbody/tr[1]/td[2]/div[1]/div[2]/form/div/table/tbody/tr[1]/td[1]/div/table[2]/tbody/tr[2]/td/select').click()
find('/html/body/table/tbody/tr[1]/td[2]/div[1]/div[2]/form/div/table/tbody/tr[1]/td[1]/div/table[2]/tbody/tr[2]/td/select/option[6]').click()

#cont. to next page
wait
find('/html/body/table/tbody/tr[1]/td[2]/div[1]/div[2]/form/div/div[2]/table/tbody/tr/td[3]/div/input').click()
driver.implicitly_wait('120')

