from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import time
import json
import os
import urllib
import pandas as pd
csv = os.path.abspath('Arizona_Louisvile_2021_Comps.CSV')
gps = pd.read_csv(csv)
gps = gps[gps['LAT'] >= 25]#and gps['LAT'] <= 49) and (gps['LNG'] >= -125 and gps['LNG'] <= -65)
gps = gps[gps['LAT'] <= 49]
gps = gps[gps['LNG'] >= -125]
gps = gps[gps['LNG'] <= -65]
gps = gps[gps['MPH'] <= 65]
g0 = None
from math import *
ind = 0
print(max(gps.MPH))

gps.to_csv('gps.csv', index=False)
driver = webdriver.Firefox()
driver.get("https://www.gpsvisualizer.com/map_input?form=jpg&format=png")

time.sleep(10)
driver.find_element_by_partial_link_text("show advanced track options [+]").click()
elem = driver.find_element_by_name('trk_colorize')
elem.send_keys('S')
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_name('drawing_mode')
elem.send_keys('D')
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_name('uploaded_file_1')
driver.find_element_by_name('legend_steps').send_keys('10')
elem.send_keys(os.path.abspath('gps.csv'))
#elem.send_keys(os.path.abspath(input('Enter GPS data name:')))
driver.find_element_by_name('new_window').click()
driver.find_element_by_name('submitted').click()
time.sleep(30)
driver.find_element_by_partial_link_text("download").click()
action = ActionChains(driver)
action.send_keys(Keys.DOWN)
action.send_keys(Keys.ENTER)