import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

searchURL = "https://gall.dcinside.com/mgallery/board/lists/?id=godverfool&s_type=search_subject_memo&s_keyword=chunklist"
searchHtml = requests.get(searchURL, headers=headers).text
searchSoup = BeautifulSoup(searchHtml, "html.parser")

TopicURL = searchSoup.find("table", {"class": "gall_list empty"})
URLs = TopicURL.find_all("a")