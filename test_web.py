from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get('https://baidu.com/')
browser.maximize_window()#全屏
username = browser.find_element_by_id('kw')
username.send_keys('sqxiong')
#password = browser.find_element_by_id('password')
#password.send_keys('ZXCasdmxd1029')
username.send_keys(Keys.ENTER)