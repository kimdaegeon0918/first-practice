# 파일 기본
import os
# print(os.getcwd()) # current working directory 
# os.chdir("rpa_basic") # 작업공간 이동
# print(os.getcwd()) 
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd()) 
# os.chdir("../..") # 조부모 폴더로 이동
# print(os.getcwd()) 
# os.chdir("c:/") # 절대 경로로 이동
# print(os.getcwd()) 

# 파일 경로 만들기
# file_path = os.path.join(os.getcwd(),"my_file.txt")
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"C:\Users\velks\Documents\z\python\my_file.txt"))

# # 파일 정보 가져오기
# import time
# import datetime

# # 파일 생성 날짜
# ctime = os.path.getctime("rpa_basic/2_desktop/11_file_system.py")
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y %m %d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime("rpa_basic/2_desktop/11_file_system.py")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y %m %d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime("rpa_basic/2_desktop/11_file_system.py")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y %m %d %H:%M:%S"))

# # 파일 크기
# size = os.path.getsize("rpa_basic/2_desktop/11_file_system.py")
# print(size) 

# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir("rpa_basic"))

# 파일 목록 가져오기 (하위 폴더 모두 포함)
# result = os.walk("rpa_basic") # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
# result = os.walk(".") # 현재 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기

# print(result)

# for root, dirs, files in result:
#     print(root, dirs, files)

# 폴더 내에서 특정 파일들을 찾으려면
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root,name))

# print(result)

# *.xlsx, *.txt, 자동화*.png 등 특정 파일 찾기
# import fnmatch
# pattern = "*.py"
# result = []
# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root,name))

# print(result)

# # 주어진 경로가 파일인지 폴더인지 확인
# print(os.path.isdir("rpa_basic"))
# print(os.path.isfile("rpa_basic"))

# print(os.path.isdir("run_btn.png"))

# # 만약에 지정된 경로에 해당하는 파일,폴더가 없다면 false
# print(os.path.isfile("run_btnn.png"))

# 주어진 경로가 존재하는지 확인
# if os.path.exists("rpa_basic"):
#     print("파일 또는 폴더 존재")
# else:
#     print("존재하지 않습니다.")

# 파일 만들기
# open("new_file.txt","a").close() # 빈 파일 생성

# # 파일명 변경
# os.rename("new_file.txt","new_file_rename.txt")

# 파일 삭제
# os.remove("new_file_rename.txt")

# 폴더 생성
# os.mkdir("new_folder")

# os.makedirs("new_folder/a/b/c") # 하위 폴더를 가지는 폴더 생성

# 폴더명 변경
# os.rename("new_folder","new_folder_rename")

# 폴더 삭제
# os.rmdir("new_folder_rename") #폴더 안이 비었을 때만 삭제
import shutil # shell utilities
# shutil.rmtree("new_folders") # 폴더 안이 비어 있지 않아도 삭제

# 파일 복사하기
# 어떤 파일을 test_folder로 복사
# shutil.copy("run_btn.png","test_folder") 
# shutil.copy("run_btn.png","test_folder/copied_run_btn.png") 

# shutil.copyfile("run_btn.png","test_folder/copied_run_btn_2.png") # 대상 파일만 

# shutil.copy2("run_btn.png","test_folder/copy2.png")

# copy, copyfile : 메타정보 복사x
# copy2 : 메타정보 복사o

# 폴더 복사
# shutil.copytree("test_folder","test_folder2")

# 폴더 이동
# shutil.move("test_folder","test_folder3")
shutil.move("test_folder","test_folder_rename") #폴더명 변경효과
