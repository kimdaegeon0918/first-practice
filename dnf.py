import pyautogui
import time
import os

os.startfile('C:\\Users\\velks\\Documents\\z\\gg\\1던.txt')

pyautogui.hotkey('win','2')
time.sleep(1)
fw = pyautogui.getActiveWindow()  

if fw.isMaximized == False:
    fw.maximize()
    
# pyautogui.hotkey('alt','d')
# pyautogui.press('d')
# pyautogui.press('enter')
# time.sleep(3)

pyautogui.hotkey('ctrl','t')
pyautogui.hotkey('alt','d')
pyautogui.write('https://df.nexon.com/df/member/login?redirectTo=https%3A%2F%2Fdf.nexon.com%2Fdf%2Fhome')
pyautogui.press('enter')
# time.sleep(5)

# pyautogui.moveTo(1500,720) # 로그인
# pyautogui.click()
# time.sleep(3)

pyautogui.moveTo(1000,800)  # 아이디
# pyautogui.click()
# time.sleep(3)

# pyautogui.moveTo(1500,500) #시작 
# pyautogui.click()