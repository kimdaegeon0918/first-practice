import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창 정보 (VSCode)
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
# pyautogui.click(fw.left + 25, fw.top + 20)

# for w in pyautogui.getAllWindows():
#     print(w) # 모든 창 가져오기

# for w in pyautogui.getWindowsWithTitle("계"):
#     print(w)

w = pyautogui.getWindowsWithTitle("파이")[0]
print(w)
if w.isActive == False:
    w.activate()    

if w.isMaximized == False:
    w.maximize()

# if w.isMinimized == False:
#     w.minimize()

pyautogui.sleep(1)

w.restore() 

w.close()