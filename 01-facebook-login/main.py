from selenium import webdriver
from time import sleep

# browser_driver = webdriver.Chrome(executable_path='/Users/elminaiusifova/Desktop/Python/week6-python-selenium-task-ElminaIusifova/chromedriver')
browser_driver = webdriver.Chrome(executable_path='./chromedriver')
browser_driver.get('https://www.facebook.com/')

browser_driver.find_element_by_name('email').send_keys('elminaapple@gmail.com')
browser_driver.find_element_by_id('pass').send_keys('Elmina@1988!')
browser_driver.find_element_by_css_selector('#loginbutton').click()

sleep(10)

browser_driver.close()