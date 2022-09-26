from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
import csv
import time
from selenium.webdriver.support.ui import WebDriverWait
import json

search = "garage door repair provo utah"
pages = 2

header = ["data_cid", "title", "address", "website", "phone", "rating","reviews","image","category","timing","description","profiles"]
data = []

# options = webdriver.FirefoxOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# #options.headless = True
# driver = webdriver.Firefox(options=options)
# options = webdriver.FirefoxOptions()
# #options.headless = True

# driver = webdriver.Firefox(executable_path='D:\my projects\geckodriver.exe', options=options) 

s=Service(r'D:\my projects\geckodriver.exe')
driver = webdriver.Firefox(service=s)
wait = WebDriverWait(driver, 5)

driver.get('https://www.google.com/maps')

driver.implicitly_wait(2)
driver.find_element(By.NAME,"q").send_keys(search + Keys.ENTER)
# more = driver.find_element(By.TAG_NAME,"g-more-link")
# more_btn = more.find_element(By.TAG_NAME,"a")
# more_btn.click()
# time.sleep(10)


elements = driver.find_elements(By.CLASS_NAME, 'id-scene')
print(elements)
counter = 1
for element in elements:
    # data_cid = element.get_attribute('data-cid')
    # element.click()
    # print('item click... 5 seconds...')
    # time.sleep(5)

    #title
    # title = element.get_attribute("aria-label")

    # print(title)

    # #phone
    # try:
    #     temp_obj = driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="kc:/collection/knowledge_panels/has_phone:phone"] span:nth-child(2) > span > a > span')
    #     if len(temp_obj.text) > 0:
    #         phone = temp_obj.text
    # except NoSuchElementException:
    #     phone =""

    # print('phone:', phone)
    title= element.find_element(By.CLASS_NAME,'Nv2PK')
    #title=element.get_attribute("aria-label")
    print(title)
    phone = element.find_element(By.CLASS_NAME,'W4Efsd').text.split(' · ')[-1]
    print(title,phone)
    row = [title, phone]
    data.append(row)
    counter+=1
    try:
        page_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Page ' + str() + '"]')
        page_button.click()
        print('page click... 10 seconds...')
        time.sleep(10)
    except NoSuchElementException:
        print('no next page')
        break

with open('garage.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)