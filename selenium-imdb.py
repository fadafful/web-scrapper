from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://google.com')

box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
box.send_keys('top 100 movies of all time')
box.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a').click()
time.sleep(10)

driver.execute_script('return document.body.scrollHeight')
driver.execute_script('window.scrollTo(0, 10500)')

driver.save_screenshot('C:/Users/Admin/Web Scrapping/sreenshot50thmovie.png')
driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li[50]/div[1]/div/div/div[1]/div[2]/div[1]/a').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div[1]/div/a/div').screenshot('C:/Users/Admin/Web Scrapping/sreenshot50thmoviecover.png')