import requests
from bs4 import BeautifulSoup

basic_URL ='https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=187940&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='

comment_list = []
for page in range(1,2614) :
    print(f"page : {page}")
    URL = basic_URL + str(page)
    html = requests.get(URL).text
    soup = BeautifulSoup(html, 'html.parser')

    score_result = soup.find("div", {"class":"score_result"})
    all_lis = score_result.find_all("li")
    for li in all_lis :
        comment = li.find("p")
        real_comment = comment.find_all("span")
        length = len(real_comment)

        if length == 1 :
            comment_list.append(comment.text.strip())
        else :
            temp = real_comment[-1]
            try :
                temp2 = temp.find('a')
                comment_list.append(temp2['data-src'])
            except :
                comment_list.append(temp.text.strip())


with open("movie_comments.txt", "w") as f: #앞에 경로를 써주면 그 경로에 저장이 됨
    for single_comments in comment_list :
        f.write(single_comments+"\n")

print("저장 완료")




    # all_comments = soup.find_all("div", {"class":"score_reple"})
    # for single_comments in all_comments :
    #     print(single_comments)
    # print(len(single_comments))


