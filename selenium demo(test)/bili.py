#coding=utf-8
from selenium import webdriver
import time
wf=webdriver.Firefox()
wf.get("http://www.bilibili.com")
wf.implicitly_wait(2)
handle=wf.current_window_handle
print(handle)
wf.find_element_by_id("search-keyword").send_keys("王老菊")
wf.find_element_by_class_name("search-submit").click()
wf.implicitly_wait(2)
handle_all=wf.window_handles
print(handle_all)
wf.switch_to_window(handle_all[1])
wf.find_element_by_xpath("html/body/div[5]/ul/li[3]/div/div[1]/a").click()
handle_all=wf.window_handles
print(handle_all)
wf.switch_to_window(handle_all[2])
time.sleep(5)
wf.maximize_window()
wf.quit()
