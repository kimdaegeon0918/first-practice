

from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

#페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

#지정한 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,1080)")
# browser.execute_script("window.scrollTo(0,2080)")

#화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

import time
interval = 2

#현재 문서 높이를 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

#반복 수행
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height
    
import requests
from bs4 import BeautifulSoup 

soup = BeautifulSoup(browser.page_source,"lxml")

# movies = soup.find_all("div",attrs={"class":["ImZGtf mpg5gc","Vpfmgd"]})
movies = soup.find_all("div",attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title)

    #할인 전 가격
    original_price = movie.find("span",attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title,"<할인되지 않은 영화 제외")
        continue

    #할인 된 가격
    price = movie.find("span",attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    #링크 정보
    link = movie.find("a",attrs={"class":"JC71ub"})["href"]
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ","https://play.google.com"+link)
    print("-" * 100)

browser.quit()