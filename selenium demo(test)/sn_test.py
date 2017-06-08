#coding=utf-8

from selenium import webdriver
import time
#inject webdriver base
wd=webdriver.Firefox()
#use the firefox moudle
time.sleep(2)
wd.get("http://www.baidu.com")
time.sleep(2)
wd.get("https://www.processon.com")
time.sleep(2)
wd.refresh()
time.sleep(4)
wd.maximize_window()
time.sleep(3)
wd.back()
time.sleep(2)
wd.forward()
time.sleep(30)
wd.get_screenshot_as_file('sc.jpg')
wd.close()