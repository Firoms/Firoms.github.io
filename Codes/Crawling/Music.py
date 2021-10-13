import requests
from bs4 import BeautifulSoup

base_URL = (
    "https://music.naver.com/listen/top100.nhn?domain=TOTAL_V2&page="  # 노래 차트 페이지 주소
)
id_list = []  # id 번호를 담는 리스트
song_title_list = []  # 노래 제목을 담는 리스트
cnt = -1  # 노래 제목과 가사를 매칭시키기 위한 카운트 변수 (순서대로 노래 제목을 입력함)
for i in range(1, 3):  # 1~2 페이지에서
    song_list = []  # 노래이름을 저장하는 리스트
    URL = base_URL + str(i)  # 인터넷 페이지를 변경해 줌
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")  # html에서 가져옴
    song_list = soup.find_all("td", {"class": "name"})[
        1:
    ]  # 노래를 모두 가져옴 (단, 2번째부터 가져옴, 1번째는 이상한 코드가 나와 임의로 수정함)

    for single_song in song_list:  # 노래 중 하나씩
        song_titles = single_song.find("span", "ellipsis")  # 제목을 song_titles 에 저장함
        song_title_list.append(song_titles.text)  # song title list 에 제목을 추가함
        # print(song_titles.text)
    track_id = soup.find_all("a", {"class": "_lyric"})  # 노래 번호들을 모두 찾아 저장함
    for single_id in track_id:  # 노래번호들중 번호 하나씩
        num = single_id["class"][
            -1
        ]  # 클래스가 여러개인 경우 클래스중 몇번째를 가져올지 선택해야하는데 맨 뒤에 번호가 있기 때문에
        # 맨 뒤에 있는 번호 부분을 저장하였다
        # num = num[::-1]
        # num = num[:8]
        # num = num[::-1]
        num = num.split(":")[-1]  # 역시 코드부분과 숫자부분을 분리하여 숫자부분만 저장한다
        id_list.append(num)  # id list 에 모든 노래의 id숫자를 추가하였다.

base_URL = "https://music.naver.com/lyric/index.nhn?trackId="  # 가사가 나오는 url로 변경한다.
for id in id_list:  # 기준으로 노래 변경 / id list에 저장되어 있는 id 숫자를 이용하여 노래를 변경한다.
    cnt += 1  # 몇번째 제목인지 세어주는 역할을한다.
    URL = base_URL + id
    html = requests.get(URL).text  # url을 가사페이지로 바꾸어준다
    soup = BeautifulSoup(html, "html.parser")
    lyric = soup.find("div", {"id": "lyricText"})  # 가사부분의 코드를 모두 찾아낸다.
    final_lyric = ""  # 한 노래의 총 가사를 저장하는 변수이다.
    for single_row in lyric:  # 가사 코드 한줄마다
        try:
            single_row = single_row.replace(
                "<br/>", "\n"
            )  # 코드에 <br/>은 엔터역할이기에 이것을 \n으로 replace 해주었다.
            # print(single_row)
            final_lyric += single_row  # 각 가사 한줄을 모아 하나의 노래가사를 만든다.
        except:
            final_lyric += "\n"  # <br/> 이 없는 경우를 대비해 예외로 추가사항을 넣었다.

    title = song_title_list[cnt]  # cnt 번째 제목을 가져온다 (cnt는 위에서 1씩 늘어나기에 제목도 함께바뀜)
    title = title.replace("?", "")  # ?는 파일명으로 사용할수 없기에 임의로 공백으로 바꾸어준다.
    with open(
        f"{title}.txt", "w", -1, "utf-8"
    ) as f:  # 파일로 저장하는 과정인데, 한국어는 오류가나서 -1,"utf-8"을 붙여 해결하였다ㅏ.
        f.write(final_lyric)  # 파일에 곡 가사를 입력하여 준다.


# song_list = soup.find_all("span", {"class":"ellipsis"})
#
# for song in song_list :
#     print(song.text.strip())
