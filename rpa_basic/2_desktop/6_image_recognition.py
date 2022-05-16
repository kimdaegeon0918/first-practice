import pyautogui

file_menu = pyautogui.locateOnScreen("file_menu.png")
print(file_menu)
pyautogui.click(file_menu)

# 속도 개선
# 1. GrayScale 
#   흑백으로 전환후 검색 grayscale=True
# 2. 범위 지정
#   region=(x, y, width, height)
# 3. 정확도 조정
#   confidence=0.x
# 자동화 대상이 바로 보여지지 않는 경우

