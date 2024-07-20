from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
import pandas as pd


#******************driver setup and URL opens************************************************************

driver = webdriver.Chrome() 
driver.get('https://www.redbus.in') 
driver.maximize_window()
time.sleep(3) 

Allstates=[]
#****************** Getting all statesnames and clicking andhra transport link *****************************************

showallstates= driver.find_element(By.XPATH,'//*[@id="homeV2-root"]/div[3]/div[1]/div[2]/a')
actions = ActionChains(driver)
actions.move_to_element(showallstates).perform()
showallstates.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

#andhraPradeshBuses= driver.find_element(By.XPATH, "/html/body/div[1]/div/article[2]/div/div/ul[1]/li[6]/a").click()
# andhraPradeshBuses   = "/html/body/div[1]/div/article[2]/div/div/ul[1]/li[6]/a"
# Allstates.append(andhraPradeshBuses)
MegalayaBuses   = "/html/body/div[1]/div/article[2]/div/div/ul[4]/li[3]/a"
Allstates.append(MegalayaBuses)
BiharBuses = "/html/body/div[1]/div/article[2]/div/div/ul[2]/li[7]/a"
Allstates.append(BiharBuses)
WBBuses = "/html/body/div[1]/div/article[2]/div/div/ul[2]/li[4]/a"
Allstates.append(WBBuses)
NBBuses = "/html/body/div[1]/div/article[2]/div/div/ul[2]/li[5]/a"
Allstates.append(NBBuses)
AssamBuses = "/html/body/div[1]/div/article[2]/div/div/ul[4]/li[5]/a"
Allstates.append(AssamBuses)
PunjabBuses = "/html/body/div[1]/div/article[2]/div/div/ul[3]/li[7]/a"
Allstates.append(PunjabBuses)
RSRTCBuses = "/html/body/div[1]/div/article[2]/div/div/ul[3]/li[3]/a"
Allstates.append(RSRTCBuses)
UPBuses = "/html/body/div[1]/div/article[2]/div/div/ul[3]/li[5]/a"
Allstates.append(UPBuses)
KeralaBuses = "/html/body/div[1]/div/article[2]/div/div/ul[1]/li[5]/a"
Allstates.append(KeralaBuses)
ChandigarhBuses = "/html/body/div[1]/div/article[2]/div/div/ul[3]/li[6]/a"
Allstates.append(ChandigarhBuses)

for onestate in Allstates:
    
    try:
        governmentBusInfoLoad = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,onestate)))
        governmentBusInfoLoad.click()        
    except StaleElementReferenceException:
        governmentBusInfoLoad = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,onestate)))
        governmentBusInfoLoad.click()

    time.sleep(3)

    #************************Getting all routes in all pages **************************************************************

    outerList = []
    andhraroutes=driver.find_elements(By.CLASS_NAME, "route")
    for b in andhraroutes:
        print(b.text)

    page=driver.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[12]/div[1]')
    actions.move_to_element(page).perform()

    pagination = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.DC_117_paginationTable"))
    )

    pagenum = pagination.find_elements(By.CSS_SELECTOR, "div.DC_117_pageTabs ")

    totalpages = len(pagenum)

    for page in range(1, totalpages + 1):
            
            time.sleep(3)
            if page >1:
                page_number_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='DC_117_pageTabs ' and text()='{page}']")))    
                driver.execute_script("arguments[0].click();", page_number_element)
                #time.sleep(3)
                
            #elif page ==1:        
            routeList = driver.find_elements(By.CSS_SELECTOR, "div.route_details")
            nextPageRouteList = []
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
    #**********************************************************
    print(len(routeName))
    print("nextPageRouteList",len(nextPageRouteList))
    print("outerList",len(outerList))
    print("len(outerList)",len(outerList))
    routeCounter = 0
    for routeListCount in outerList:
        routeCounter += 1
        driver.get(routeListCount[1])
        time.sleep(5)
        print("routeCounter ",routeCounter)
        try:
            tempBusCount = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.f-bold.busFound")))
            print("busCount", tempBusCount.text) 
            temp = tempBusCount.text 
            BusCount = int(temp.split()[0])
            try :
                view_buses_buttons = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='button' and normalize-space()='View Buses']")))
                print("view_buses_buttons",len(view_buses_buttons))
                if len(view_buses_buttons) ==2:
                    busViewClick = driver.find_elements(By.CSS_SELECTOR, "div.button")
                    body=driver.find_element(By.TAG_NAME,'body')
                    body.send_keys(Keys.DOWN)
                    time.sleep(2)
                    #actions.move_to_element(busViewClick[1]).perform()
                    time.sleep(5)
                    busViewClick[1].click()
                    time.sleep(3)
                    busViewClick[0].click()
                    time.sleep(3)
                elif len(view_buses_buttons) ==1:
                    busViewClick = driver.find_elements(By.CSS_SELECTOR, "div.button")
                    body=driver.find_element(By.TAG_NAME,'body')
                    body.send_keys(Keys.DOWN)
                    time.sleep(2)
                    #actions.move_to_element(busViewClick[1]).perform()
                    time.sleep(5)
                    busViewClick[0].click()
                    time.sleep(3)
            except TimeoutException as e:
                    print("In this Route has No any government buses are available")

    #******************* Scrolling full page ******************************************************************
            scroll_attempts = 0
            tempBusCount = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.f-bold.busFound")))
            print("busCount", tempBusCount.text) 
            temp = tempBusCount.text 
            BusCount = int(temp.split()[0])
            max_attempts = int(BusCount/7.5)

            while scroll_attempts < max_attempts:
                driver.execute_script("window.scrollBy(0, 3000);")
                #time.sleep(1)
                scroll_attempts += 1
                #print(f"Scroll attempt {scroll_attempts}")

    #******************* Fetching all 10 column values ********************************************************
            busname = driver.find_elements(By.CSS_SELECTOR, "div.travels.lh-24.f-bold.d-color")  # TEXT
            bustype = driver.find_elements(By.CSS_SELECTOR, "div.bus-type.f-12.m-top-16.l-color.evBus")  # TEXT
            departing_time = driver.find_elements(By.CSS_SELECTOR, "div.dp-time.f-19.d-color.f-bold")  # DATETIME
            duration = driver.find_elements(By.CSS_SELECTOR, "div.dur.l-color.lh-24")  # TEXT
            reaching_time = driver.find_elements(By.CSS_SELECTOR, "div.bp-time.f-19.d-color.disp-Inline")  # DATETIME
            star_rating=driver.find_elements(By.CSS_SELECTOR,"div[class='column-six p-right-10 w-10 fl']")  # FLOAT
            price = driver.find_elements(By.CSS_SELECTOR, "div.seat-fare")  # DECIMAL
            seats_available = driver.find_elements(By.CSS_SELECTOR, "div.column-eight.w-15.fl")

            time.sleep(5)
            driver.back()
            time.sleep(5)
            driver.back()
            time.sleep(5)
        except TimeoutException as e:
            print("Temporarily No buses are available on this route")
            time.sleep(5)
            driver.back()
            time.sleep(5)
            driver.back()
            time.sleep(5)
print(len(routeName))
print(len(routeLink))
print(len(busname))
print(len(bustype))
print(len(departing_time))
print(len(duration))
print(len(reaching_time))
print(len(star_rating))
print(len(price))
print(len(seats_available))
