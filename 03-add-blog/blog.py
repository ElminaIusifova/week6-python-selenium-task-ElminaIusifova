from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

browser_driver = webdriver.Firefox(executable_path='/Users/elminaiusifova/Desktop/Python/week6-python-selenium-task-ElminaIusifova/geckodriver')

browser_driver.get('http://35.225.243.133/admin/login/')

browser_driver.find_element_by_name('username').send_keys('student')
browser_driver.find_element_by_id('id_password').send_keys('qatester')
browser_driver.find_element_by_css_selector('#login-form > div.submit-row > input[type=submit]').click()

sleep(3)

browser_driver.find_element_by_css_selector('#content-main > div > table > tbody > tr.model-blog > td:nth-child(2) > a').click()

sleep(3)

browser_driver.find_element_by_css_selector('#container > div.breadcrumbs > a:nth-child(1)').click()

sleep(3)

browser_driver.find_element_by_css_selector('#content-main > div > table > tbody > tr.model-blogger > td:nth-child(2) > a').click()

sleep(3)

browser_driver.find_element_by_name('full_name').send_keys('Ali Alireza')

sleep(3)

browser_driver.find_element_by_css_selector('#blogger_form > div > div > input.default').click()
sleep(3)

browser_driver.close()

