# pillow 다운로드
# 맞출때까지 , 맞추면 +1 틀리면 점수 출력 후 종료
import random
import os
from PIL import Image

path = os.path.join(os.getcwd(), "champ images")
file_list = os.listdir(path)

ans_dic = {}

for single_file in file_list:
    ans_dic[single_file] = single_file.split(".")[0]
scr = 0
i = 1

while i == 1:
    rand_num = random.randrange(len(ans_dic))
    filename = file_list[rand_num]
    file_path = os.path.join(path, file_list[rand_num])
    ans = ans_dic[filename]
    image = Image.open(file_path)
    image.show()
    print("이 사진의 챔프는 누구일까요?")
    ip = input()
    if ip == ans:
        print("정답입니다.")
        print("1점을 획득합니다.")
        print("다음 문제입니다.")
        scr += 1
    else:
        print("틀렸습니다.")
        print("정답은", ans, "입니다.")
        break

print("당신의 점수는", scr, "점 입니다.")
