from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
import time 
import string
import openpyxl
import os
from selenium.webdriver.firefox.service import Service


s=Service(r'D:\my projects\geckodriver.exe')
driver = webdriver.Firefox(service=s)
wait = WebDriverWait(driver, 5)

#Opening Google maps 
url='https://www.google.com/maps'
driver.get(url)

#Finding the search box
searchbox=driver.find_element(By.ID,'searchboxinput')
location= "garage door repair provo utah"
searchbox.send_keys(location)
searchbox.send_keys(Keys.ENTER)
time.sleep(2)

#Locating the results of the search
entries=driver.find_elements(By.CLASS_NAME,'hfpxzc')
print(entries)

#Prepare the excel file using the Openpyxl  
wb= openpyxl.load_workbook(r'D:\my projects\Google-map-scrap-using-Flask-py\garages.xlsx')
sheetname=wb.sheetnames
sheet=wb[sheetname[0]]
sheet.title ="garages"



#Extracting the information from the results  
for entry in entries:
    #Empty list 
    labels=[]
    #Extracting the Name, adress, Phone, and website:
    
    name= entry.get_attribute("aria-label")
    phone = entry.find_element(By.CLASS_NAME,'section-result-hours-phone-container').text.split(' · ')[-1]
    #Try/except  to write the extracted info in the Excel file pass if doessn't exist 
    try:
        sheet.append([location,name,phone])
    except IndexError:
        pass
 
#saving the excel file 
wb.save("garages.xlsx")