from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:/Users/rac/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver.get('chrome://settings/clearBrowserData')
driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)