from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#from webdriver_manager.chrome import ChromeDriverManager
# No need for chrome web driver

driver = webdriver.Chrome()
driver.get("https://goat.com/sneakers")

#click
driver.find_element(By.XPATH, '//*[@id="grid-header-description"]/div/p/a[1]').click()

#input text
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')

box.send_keys('how to be rich')
box.send_keys(Keys.ENTER)

#take screenshot
driver.save_screenshot('C:/Users/Admin/Web Scrapping/sreenshot.png')
driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[18]/a[1]/div[1]/img').screenshot('C:/Users/Admin/Web Scrapping/sreenshot2.png')

#self scroll
driver.execute_script('return document.body.scrollHeight')
driver.execute_script('window.scrollTo(0, 1783)')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    break
    
#wait times
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_condition as EC
import time

box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
box.send_keys('how to be rich')
box.send_keys(Keys.ENTER)
#wait for 3 seconds without any condition
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="bqHHPb"]/div/div/div[1]/a[2]').click()

#wait for a 10s for a specific id, xpath etc before clicking // not working
#element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID, 'hdtb-msb'))



