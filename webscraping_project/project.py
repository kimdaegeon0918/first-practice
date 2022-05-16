import re
import requests
from bs4 import BeautifulSoup
# from requests.models import encode_multipart_formdata

def create_soup(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    return soup

def weather(): 
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EA%B7%80%ED%8F%AC%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&tqi=hUukcsp0J1ZssQem8JRssssstYd-338896"
    soup = create_soup(url)

    # 위치 정보
    city = soup.find("h2",attrs={"class":"title"}).get_text()
    
    # 흐림, 어제보다 00℃ 높아요
    cast = soup.find("p",attrs={"class":"summary"}).get_text()

    # 현재 00℃ (최저 00℃ / 최고 00℃)
    curr_temp = soup.find("div",attrs={"class":"temperature_text"}).get_text().replace("현재 온도","").strip()
    min_temp = soup.find("span",attrs={"class":"lowest"}).get_text().replace("최저기온","")
    max_temp = soup.find("span",attrs={"class":"highest"}).get_text().replace("최고기온","")

    # 오전 강수확률 00% / 오후 강수확률 00%
    rain_rate = soup.find_all("span",attrs={"class":"rainfall"})
    rain_rate_morning = rain_rate[0].get_text()
    rain_rate_afternoon = rain_rate[1].get_text()

    # 미세먼지 00㎍/㎥ 좋음
    # 초미세먼지 00㎍/㎥ 좋음
    dust = soup.find_all("span",attrs={"class":"txt"})
    dust1 = dust[0].get_text()
    dust2 = dust[1].get_text()

    #출력
    print(city)
    print(cast)
    print("현재 {} (최저 {} / 최고 {}).".format(curr_temp,min_temp,max_temp))
    print("오전 강수확률 {} / 오후 강수확률 {}".format(rain_rate_morning,rain_rate_afternoon))
    print("미세먼지 {} / 초미세먼지 {}".format(dust1,dust2))

def headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul",attrs={"class":"hdline_article_list"}).find_all("li" , limit=3)
    for index,news in enumerate(news_list):
        title = news.div.a.get_text().strip()  #news.find("a") 도 같은결과
        link = url + news.find("a")["href"]
        print("{}. {}".format(index+1,title))
        print("  (링크 : {}".format(link))
    print()

def it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li" , limit=3)
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1
        title = news.find_all("a")[a_idx].get_text().strip()
        link = news.find("a")["href"]
        print("{}. {}".format(index+1,title))
        print("  (링크 : {}".format(link))
    print()

def english():
    print("[오늘의 영어 회화]")    
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div",attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]: 
        print(sentence.get_text().strip())
    
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())
if __name__ == "__main__":
    weather()        #오늘의 날씨정보 가져오기
    # headline_news()
    it_news()
    english()      