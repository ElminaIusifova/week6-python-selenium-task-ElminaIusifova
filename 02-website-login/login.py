from selenium import webdriver
from time import sleep

browser_driver = webdriver.Firefox(executable_path='/Users/elminaiusifova/Desktop/Python/week6-python-selenium-task-ElminaIusifova/geckodriver')

browser_driver.get('http://35.225.243.133/admin/login/')

browser_driver.find_element_by_name('username').send_keys('student')
browser_driver.find_element_by_id('id_password').send_keys('qatester')
browser_driver.find_element_by_css_selector('#login-form > div.submit-row > input[type=submit]').click()



sleep(10)

browser_driver.close()