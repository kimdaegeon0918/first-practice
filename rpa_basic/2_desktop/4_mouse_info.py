import pyautogui
# pyautogui.FAILSAFE = False # 마우스를 귀퉁이에 넣으면 종료되는 옵션 끄기
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
# pyautogui.mouseInfo()

for i in range(5):
    pyautogui.move(100,100)
    