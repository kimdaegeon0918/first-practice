import pyautogui
import time
import os

os.startfile('C:\\Users\\velks\\Documents\\z\\gg\\1.txt')

pyautogui.hotkey('win','2')
time.sleep(1)
w = pyautogui.getWindowsWithTitle("chrome")[0]