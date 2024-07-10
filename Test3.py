from selenium import webdriver 
#from selenium.webdriver.common.Keys import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time
import pandas as pd


driver = webdriver.Chrome() 
driver.get('https://www.redbus.in') 
time.sleep(5) 

element= driver.find_element(By.XPATH,'//*[@id="Carousel"]')
elements= driver.find_elements(By.XPATH,'//*[@id="Carousel"]')
statebusname= driver.find_elements(By.CLASS_NAME, "rtcName")
#statebusroutenum= driver.find_elements(By.CLASS_NAME, "sc-kvZOFW ekNeom")
andhrabuses=driver.find_element(By.XPATH,'//*[@id="Carousel"]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')

#bus_data={}
#bus_data.update({'statebusname' : statebusname#,
		#'statebusroutenum': statebusroutenum
		#})


actions = ActionChains(driver)
actions.move_to_element(element).perform()
andhrabuses.click()
time.sleep(5)
routename= driver.find_elements(By.CLASS_NAME, "route")
for j in routename:
	print(j.text)

routename[0].click()
time.sleep(5)

totalpvtbuslist= driver.find_elements(By.CLASS_NAME, "travels lh-24 f-bold d-color")
APSRTCviewbuses=driver.find_element(By.XPATH,'//*[@id="result-section"]/div[1]/div/div[2]/div/div[4]/div[2]')
APSRTCviewbuses.click()
time.sleep(5)
APSRTCviewbuses=driver.find_elements(By.CLASS_NAME, "travels lh-24 f-bold d-color")

#statedf=pd.DataFrame(elements)

for a in APSRTCviewbuses:
	print(APSRTCviewbuses[a].text)

print("All good")
driver.quit()