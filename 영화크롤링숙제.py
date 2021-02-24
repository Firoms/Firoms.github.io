import requests
from bs4 import BeautifulSoup

basic_URL = "https://movie.daum.net/moviedb/grade?movieId=133855&type=netizen&page="

comment_list = []
for page in range(1, 503):
    print(f"page : {page}")
    URL = basic_URL + str(page)
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")

    score_result = soup.find("p", {"class": "desc_review"})
    comment_list.append(score_result.text.strip())


with open("movie_comments.txt", "w") as f:
    for single_comments in comment_list:
        f.write(single_comments + "\n")

print("저장 완료")
