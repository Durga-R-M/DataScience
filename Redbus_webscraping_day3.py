from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd


#******************driver setup and URL opens************************************************************

driver = webdriver.Chrome() 
driver.get('https://www.redbus.in') 
time.sleep(3) 

#****************** Getting all statesnames and clicking andhra transport link *****************************************

element= driver.find_element(By.XPATH,'//*[@id="Carousel"]')
statebusname= driver.find_elements(By.CLASS_NAME, "rtcName")

#for a in statebusname:
	#print(a.text)

andhracard=driver.find_element(By.XPATH,'//*[@id="Carousel"]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')
actions = ActionChains(driver)
actions.move_to_element(element).perform()
andhracard.click()
time.sleep(5)

page=driver.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[12]/div[1]')
actions.move_to_element(page).perform()
#page.click()
time.sleep(5)

andhraroutes=driver.find_elements(By.CLASS_NAME, "route")
for b in andhraroutes:
	print(b.text)
#andhraroutes[0].click()
time.sleep(10)

pagination = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.DC_117_paginationTable"))
)

page_numbers = pagination.find_elements(By.CSS_SELECTOR, "div.DC_117_pageTabs ")

total_pages = len(page_numbers)

for page in range(2, total_pages + 1):
    
    time.sleep(3)
 
    page_number_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='DC_117_pageTabs ' and text()='{page}']")))    
    driver.execute_script("arguments[0].click();", page_number_element)
    time.sleep(3)
    
 
    routeList = driver.find_elements(By.CSS_SELECTOR, "div.route_details")
    print("2nd_Route List",len(routeList))
    nextPageRouteList = []
    outerList = []
    for info in routeList:
        innerList = []
        anchor = info.find_element(By.CSS_SELECTOR, "a.route")
        routeName = anchor.text
        routeLink = anchor.get_attribute('href')
        
        innerList.append(routeName)
        innerList.append(routeLink)
        nextPageRouteList.append(innerList)

    for load in nextPageRouteList:
        outerList.append(load)

"""APSRTCbusview=driver.find_element(By.XPATH,'//*[@id="result-section"]/div[2]/div/div[2]/div/div[4]/div[2]')
APSRTCbusview.click()
time.sleep(10)
"""



