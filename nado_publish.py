names=["유튜버1","유튜버2","유튜버3","유튜버4"]

for name in names:
    file_name=name+".txt"
    with open(file_name,"w",encoding="utf8") as mail:
        mail.write("안녕하세요? "+name+"님 \
        \n\n(주)나도출판 편집자 나코입니다.\
        \n현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.\n"\
        +name+"님의 유튜브 영상을 보고 연락을 드리게 되었습니다. \
        \n... \
        \n... \
        \n-나코 드림")
    