from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

browser_driver = webdriver.Firefox(executable_path='/Users/elminaiusifova/Desktop/Python/week6-python-selenium-task-ElminaIusifova/geckodriver')

browser_driver.get('http://35.225.243.133/admin/login/')

browser_driver.find_element_by_name('username').send_keys('student')
browser_driver.find_element_by_id('id_password').send_keys('qatester')
browser_driver.find_element_by_css_selector('#login-form > div.submit-row > input[type=submit]').click()



sleep(5)

browser_driver.get('https://google.com/')

search_input = browser_driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')

search_input.send_keys('python')

sleep(2)

browser_driver.implicitly_wait(10)

search_btn = browser_driver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
search_btn = WebDriverWait(browser_driver, 10).until(browser_driver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]'))


search_btn.click()

browser_driver.close()

