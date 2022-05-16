import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] 
w.activate()

# pyautogui.write("12345")
# pyautogui.write("nadocoding", interval=0.25)

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"],interval=0.25) 
# 키 정보는 automate the boring stuff with python 검색 후 찾아보기

# 특수 문자
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# 조합키
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 간편하게 조합키로
# pyautogui.hotkey("ctrl","alt","shift","a")
# pyautogui.hotkey("ctrl","a")

import pyperclip
pyperclip.copy("나도코딩")
pyautogui.hotkey("ctrl","v")

# 자동화 프로그램 종료
# win : ctrl + alt + del
# mac : cmd + shift + option + q