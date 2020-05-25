from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

searchKey = input('Enter What To Search : ')

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://google.com')

gSearch = driver.find_element_by_xpath('//*[@title="Search"]')
gSearch.send_keys(searchKey)
gSearch.send_keys(Keys.ENTER)

searchKey = searchKey.upper()

hLinks = driver.find_elements_by_xpath('//*[@href]')

time.sleep(2)

finalLinks = []

for link in hLinks:
    if ('google' in link.get_attribute('href')):
        pass
    elif('youtube' in link.get_attribute('href')):
        pass
    elif('gstatic' in link.get_attribute('href')):
        pass
    else:
        finalLinks.append(link)
        
wordReg = re.compile(searchKey)
        
for link in finalLinks:
    driver = webdriver.Chrome(PATH)
    driver.get(link.get_attribute('href'))
    bodyContent = driver.find_element_by_tag_name('body')
    wordList = wordReg.findall(bodyContent.text.upper())
    print(driver.title)
    print(link.get_attribute('href'))
    print('---------------------------------------------------------------------------------------------------------')
    print(f'No. of times : {len(wordList)}')
    print(' ')
    print(' ')
    time.sleep(2)
    driver.quit()
    
print('...........FINISHED...........')