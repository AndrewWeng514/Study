import time

import pyautogui


class Img:
    def __init__(self):
        pass

    def find_img(self, img):
        time.sleep(2)
        x, y = pyautogui.locateCenterOnScreen(img)
        # print(x,y)
        return x, y

    def click(self, img):
        x, y = self.find_img(img)
        time.sleep(2)
        pyautogui.click(x, y)

    def input(self, img, content):
        self.click(img)
        time.sleep(1)
        pyautogui.typewrite(content, interval=0.5)
        pyautogui.press('enter')


if __name__ == '__main__':
    im = Img()
    time.sleep(3)
    x, y = im.find_img('username.png')
