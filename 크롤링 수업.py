'''
requests와 BeautifulSoup를 이용하여 Crawling하는 경우에는
bs4와 requests 라이브러리를 install 해야한다.
'''
import requests
from bs4 import BeautifulSoup

base_URL = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=경기도"


user_input = input()
URL = base_URL + user_input + "날씨"

html = requests.get(URL).text

soup = BeautifulSoup(html, "html.parser")

info = soup.find("p", {"class": "cast_txt"}).text
print(info)
# min = soup.find("span", {"class":"min"}).text
# print(min)
# max = soup.find("span", {"class":"max"}).text
# print(max)


# min = soup.find("span", {"class":"min"})
# min_num = min.find("span", {"class":"num"}).text
# print(min_num)

temp_list = soup.find_all("span", {"class": "num"})
temp_list = temp_list[0:2]
# print(type(temp_list))

for single_temp in temp_list:
    print(single_temp.text)
