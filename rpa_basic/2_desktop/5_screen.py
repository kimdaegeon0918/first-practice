import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 28,20 54,166,242 #36A6F2

pixel = pyautogui.pixel(28,20)
print(pixel)    

# print(pyautogui.pixelMatchesColor(28,20,(54,166,242)))
print(pyautogui.pixelMatchesColor(28,20,pixel))
