# facebook login

Create a bot with a login on Facebook with your personal account information.




from selenium import webdriver
from time import sleep

browser_driver = webdriver.Firefox(executable_path='/home/idris/PythonProjects/selenium_example/geckodriver')

browser_driver.get('http://35.225.243.133/admin/login/')

browser_driver.find_element_by_name('username').send_keys('tester')
browser_driver.find_element_by_id('id_password').send_keys('idris1234')
browser_driver.find_element_by_css_selector('#login-form > div.submit-row > input[type=submit]').click()

## id #
## tag 
## class .
#login-form > div.submit-row > input[type=submit]


sleep(10)

browser_driver.close()