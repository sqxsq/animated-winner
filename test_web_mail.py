from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get('https://mail.fiberhome.com')
#
browser.switch_to_window(browser.window_handles[-1])
browser.maximize_window()
username = browser.find_element_by_id('uid')
username.send_keys('sqxiong')
#或browser.find_element_by_id('uid').send_keys('sqxiong')
#或browser.find_element_by_xpath('//input[@id="uid"]').send_keys("sqxiong")
password = browser.find_element_by_id('password')
password.send_keys('ZXCasdmxd1029')
#或browser.find_element_by_id('password').send_keys('ZXCasdmxd1029')
#或browser.find_element_by_xpath('//input[@id="password"]').send_keys("ZXCasdmxd1029")


password.submit()#或password.send_keys(Keys.ENTER)
#这句不对browser.find_element_by_xpath('//input[@name="action:login"]').click()
