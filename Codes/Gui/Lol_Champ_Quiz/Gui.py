# cui : console User interface
# gui : Graphic user interface
import os
import random

from tkinter import *  # *은 모든 내용을 임포트한다는 뜻
from PIL import ImageTk  # pillow & tkinter 다운

# print(os.getcwd())

img_path = os.path.join(os.getcwd(), "champ images")
img_list = os.listdir(img_path)  # list 형태로 파일 이름 리턴


# {가렌.jpg :가렌, }
ans_dic = {}
for img in img_list:
    # name = img[::-1]
    # name = name[4:]
    # name = name[::-1]
    ans_dic[img] = img.split(".")[0]
    # ans_dic[img] = name


class GameScreen:
    components = {}

    def __init__(self):
        self.display = Tk()  # 화면을 만들어줌
        self.display.title("Character Guessing Game")
        self.display.geometry("400x400")
        GameScreen.components = self.placingComponenents()
        self.display.mainloop()  # 화면을 보여줌  *맨끝에 써주기

    def placingComponenents(self):
        title = Label(
            self.display,
            text="롤 챔프 맞추기 게임",
            background="pink",
            font=("맑은 고딕", 20),
            height=3,
        )
        title.pack()  # 위에서 부터 보여줌

        describe = Label(
            self.display,
            text="사진을 보고 캐릭터의 이름을 맞추는 게임입니다.\n 얼마나 많이 맞출 수 있는지 확인해보세요",
            font=("맑은고딕", 12),
        )
        describe.place(x=30, y=180)

        game_start = Button(
            self.display,
            fg="green",
            text="Game Start",
            height=2,
            width=12,
            background="yellow",
            command=self.gamestart,
        )
        game_start.pack()

        img_label = Label(self.display)
        img_label.place(x=160, y=220)

        playField = Entry(self.display)
        playField.bind("<Return>", GameOperation.checkAns)  # return은 엔터를 입력 받았을 때를 의미함

        life_label = Label(self.display)

        return {
            "title_label": title,
            "describe_label": describe,
            "game_start_button": game_start,
            "img_label": img_label,
            "play_entry": playField,
            "life_label": life_label,
        }

    def gamestart(self):
        describe_label: Label = self.components["describe_label"]
        game_start_button: Button = self.components["game_start_button"]
        score_label: Label = self.components["title_label"]
        entry: Entry = self.components["play_entry"]
        life_label: Label = self.components["life_label"]

        describe_label.destroy()
        game_start_button.destroy()
        entry.place(x=125, y=190)
        score_label["text"] = 0
        entry.focus_set()

        life_label.place(x=0, y=0)
        life_label["text"] = "♡ ♡ ♡"

        GameOperation.placeQuiz()


class GameOperation:
    ans = ""
    score = 0
    life = 3

    @classmethod
    def placeQuiz(cls):
        img_label: Label = GameScreen.components["img_label"]
        rand_num = random.randrange(0, 147)
        img_name = img_list[rand_num]
        print(img_name)
        GameOperation.ans = ans_dic[img_name]
        final_path = os.path.join(img_path, img_name)
        character_img = ImageTk.PhotoImage(file=final_path)  # file은 file 위치
        # Label 에 이미지 설정
        img_label.configure(image=character_img)
        img_label.image = character_img

    @classmethod
    def checkAns(cls, event):
        entry: Entry = GameScreen.components["play_entry"]
        score_label: Label = GameScreen.components["title_label"]
        life_label: Label = GameScreen.components["life_label"]
        user_input = entry.get()
        print(user_input)
        if GameOperation.ans == user_input:
            score_label["text"] = int(score_label["text"]) + 1
            GameOperation.score = score_label["text"]
            entry.delete(0, "end")
        else:
            life_label["text"] = life_label["text"][:-2]
            entry.delete(0, "end")
            GameOperation.life -= 1
            # score_label["text"] = f'틀렸습니다! \n 정답은 {GameOperation.ans}입니다.' # 시간을 멈추고 싶다면 thread를 이용해보자
        if GameOperation.life == 0:
            score_label[
                "text"
            ] = f"틀렸습니다! \n 정답은 {GameOperation.ans}입니다. \n 당신의 점수는 {GameOperation.score}점 입니다."
            entry.destroy()
        else:
            GameOperation.placeQuiz()


game = GameScreen()
