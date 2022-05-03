from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

website = 'https://www.nba.com/stats/teams/traditional/?sort=W_PCT&dir=-1&SeasonType=Regular%20Season&Season=2021-22'
path = 'chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get(website)

datos = []
time.sleep(15)
#Primera pagina
table = driver.find_element(by=By.CLASS_NAME,value='nba-stat-table__overflow')
filas = table.find_elements(by=By.TAG_NAME,value='tr')
for fila in filas:
    datos.append(fila.text)
"""
next_page_button = driver.find_element(by=By.XPATH,value='/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/a[2]')
next_page_button.click()

time.sleep(5)
#segunda pagina
table = driver.find_element(by=By.CLASS_NAME,value='nba-stat-table__overflow')
filas = table.find_elements(by=By.TAG_NAME,value='tr')
for fila in filas:
    datos.append(fila.text)

next_page_button = driver.find_element(by=By.XPATH,value='/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/a[2]')
next_page_button.click()

time.sleep(5)
#tercer pagina
table = driver.find_element(by=By.CLASS_NAME,value='nba-stat-table__overflow')
filas = table.find_elements(by=By.TAG_NAME,value='tr')
for fila in filas:
    datos.append(fila.text)

next_page_button = driver.find_element(by=By.XPATH,value='/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/a[2]/i')
next_page_button.click()
time.sleep(5)
table = driver.find_element(by=By.CLASS_NAME,value='nba-stat-table__overflow')
filas = table.find_elements(by=By.TAG_NAME,value='tr')
for fila in filas:
    datos.append(fila.text)

next_page_button = driver.find_element(by=By.XPATH,value='/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/a[2]/i')
next_page_button.click()
time.sleep(2)
table = driver.find_element(by=By.CLASS_NAME,value='nba-stat-table__overflow')
filas = table.find_elements(by=By.TAG_NAME,value='tr')
for fila in filas:
    datos.append(fila.text)

for j in range(2):
    table = driver.find_element(by=By.CLASS_NAME,value='nba-stat-table__overflow')
    filas = table.find_elements(by=By.TAG_NAME,value='tr')
    for fila in filas:
        datos.append(fila.text)    
    next_page_button = driver.find_element(by=By.XPATH,value='/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/a[2]')
    next_page_button.click()
    time.sleep(2)
"""
driver.quit()
df = pd.DataFrame({'Datos': datos})
df.to_csv('data\Data.csv',index = False)