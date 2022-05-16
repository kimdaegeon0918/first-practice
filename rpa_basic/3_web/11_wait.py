from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://flight.naver.com/')

#가는날클릭
browser.find_element_by_class_name('tabContent_option__2y4c6 select_Date__1aF7Y').click()
browser.find_elements_by_link_text('30')[0].click()

#오는날클릭
browser.find_elements_by_link_text('5')[1].click()

#제주도 클릭
browser.find_element_by_link_text('제주').click()

#항공권 검색
browser.find_element_by_class_name('searchBox_search__2KFn3').click()

time.sleep(5)
browser.quit()