#bs4 requests 다운  숙제 : 다음에서 크롤링 >> 대만 날씨 출력하기 앞에 3개 도시명 & 최저 최대 온도
# deinm@naver.com   //  010-9076-7536

import requests
from bs4 import BeautifulSoup

base_URL = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query='


user_input = input()
URL = base_URL + user_input + "날씨"

html = requests.get(URL).text

soup = BeautifulSoup(html, 'html.parser')

info = soup.find("p", {"class":"cast_txt"}).text
print(info)
# min = soup.find("span", {"class":"min"}).text
# print(min)
# max = soup.find("span", {"class":"max"}).text
# print(max)


# min = soup.find("span", {"class":"min"})
# min_num = min.find("span", {"class":"num"}).text
# print(min_num)

temp_list = soup.find_all("span",{"class":"num"})
temp_list = temp_list[0:2]
# print(type(temp_list))

for single_temp in temp_list :
        print(single_temp.text)

