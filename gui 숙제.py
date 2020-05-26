import os
import random
import time
import threading

from tkinter import *
from PIL import ImageTk

img_path = os.path.join(os.getcwd(), "축구선수 클립아트")
img_list = os.listdir(img_path)


def move():
    time.sleep(5)
    print("성공")




class GameScreen:
    def __init__(self):
        self.display = Tk()
        self.display.title("축구선수 움직이기")
        self.display.geometry("1250x900")
        GameScreen.components = self.components()
        self.display.mainloop()




    def components(self):
        img_label = Label(self.display, height = 50, width = 50)
        img_label.place(x=0 , y=0)
        img_name = img_list[0]
        final_path = os.path.join(img_path, img_name)
        character_img = ImageTk.PhotoImage(file=final_path)
        img_label.configure(image=character_img)
        img_label.image = character_img
        GameScreen.move = self.move()

    def move(self):
        for a in range(800):
            time.sleep(1)
            print(a)
            img_label = Label(self.display, height=50, width=50)
            img_label.place(x=a, y=50)
            img_name = img_list[0]
            final_path = os.path.join(img_path, img_name)
            character_img = ImageTk.PhotoImage(file=final_path)
            img_label.configure(image=character_img)
            img_label.image = character_img

    def thread(self):
        t = threading.Thread(target=move)
        t.start()







game = GameScreen()

