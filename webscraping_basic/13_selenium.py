import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe") #괄호 안에 경로입력

#1. 네이버 이동
browser.get("http://naver.com")

#2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3. id와 패스워드 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

#4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()
time.sleep(3)

#5. id를 새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

#6. html정보 출력
print(browser.page_source)

#7. browser종료
browser.quit()