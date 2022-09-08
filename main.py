import pyautogui
import pyautogui as pya
from PIL import ImageGrab
import numpy as np
import time


def jump_dino():
    for i in range(482, 544):
        for j in range(410, 425):
            # data[i, j] = 0
            if data[i, j] <= 100:
                return True


if __name__ == "__main__":
    print("It will ")
    time.sleep(3)
    pyautogui.press('up')

    while True:
        img = ImageGrab.grab().convert('L')
        data = img.load()
        if jump_dino():
            pyautogui.press('up')
            # print('jump')
    # img = ImageGrab.grab().convert('L')
    # data = img.load()
    # jump_dino()
    # img.show()

