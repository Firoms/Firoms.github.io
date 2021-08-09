import pyautogui
import time
try_num = 4
while True:
    print(try_num)
    pyautogui.moveTo(1240, 460)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(550, 800)
    time.sleep(1)
    pyautogui.click()
    time.sleep(10*((try_num/50)+1))
    try_num += 1