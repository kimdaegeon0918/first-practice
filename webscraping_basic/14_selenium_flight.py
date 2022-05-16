from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/flights"
browser.get(url)

#가는날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

#이번달 27,28일 선택
# browser.find_element_by_link_text("27")[0].click()
# browser.find_element_by_link_text("28")[0].click()

#다음달 27,28일 선택
browser.find_element_by_link_text("27")[1].click()
browser.find_element_by_link_text("28")[1].click()

#제주도 선택
browser.find_element_by_xpath("").click()

#항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"")))
    print(elem.text) #첫번째 결과 출력
finally:
    browser.quit()

#첫번째 결과 출력
# elem = browser.find_element_by_xpath("")
# print(elem.text)