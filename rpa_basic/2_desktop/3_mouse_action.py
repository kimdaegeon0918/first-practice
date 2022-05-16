import pyautogui

pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position()) # 좌표 출력

# pyautogui.click(88, 17, duration=0.5)
# pyautogui.click()
# pyautogui.mouseDown() # 누르기
# pyautogui.mouseUp() # 떼기

# pyautogui.doubleClick()
# pyautogui.click(clicks=500) 

# 마우스 드래그
# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300,300)
# pyautogui.mouseUp()

# pyautogui.rightClick()
# pyautogui.middleClick()

# print(pyautogui.position())
# pyautogui.moveTo(1122,258)
# pyautogui.drag(100,0) # 현재 위치 기준으로 이동
# pyautogui.drag(100,0, duration=0.25) # 너무빨라서 수행이 안될때 duration 사용
# pyautogui.dragTo(1222,258, duration=0.25) # 절대 좌표로 드래그

pyautogui.scroll(300) # 위 방향으로 300만큼 스크롤 / 음수이면 아래로 스크롤


