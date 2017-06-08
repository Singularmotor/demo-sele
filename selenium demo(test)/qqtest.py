#coding=utf-8
from selenium import webdriver
import time
wf=webdriver.Firefox()
wf.get("http://www.qq.com")
wf.implicitly_wait(5)
wf.find_element_by_xpath(".//*[@id='loginGrayLayout']").click()
wf.switch_to_frame("login_frame")
time.sleep(2)
wf.find_element_by_xpath(".//*[@id='switcher_plogin']").click()
time.sleep(2)
wf.find_element_by_id("close").click()
time.sleep(2)
wf.switch_to_window(wf.window_handles)
wf.find_element_by_xpath(".//*[@id='loginGrayLayout']").click()