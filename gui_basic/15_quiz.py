import os
from tkinter import *

root=Tk()
root.title("제목없음 - Windows 메모장")
root.geometry("640x480")

# root.resizable(TRUE,TRUE)

# frame=Frame(root)
# frame.pack()

scrollbar=Scrollbar(root)
scrollbar.pack(side="right",fill="y")

txt=Text(root,yscrollcommand=scrollbar.set)
txt.pack(fill="both",expand=True)

scrollbar.config(command=txt.yview)

filename="mynote.txt"

def open_file():
    if os.path.isfile(filename):
        txt.delete("1.0",END)
        with open(filename,"r",encoding="utf8") as file:
            txt.insert(END,file.read())
def save_file():
    with open(filename,"w",encoding="utf8") as file:
        # txt_file=open(filename,"w",encoding="utf8")
        file.write(txt.get("1.0",END))

menu=Menu(root)

menu_file=Menu(menu,tearoff=0)
menu_file.add_command(label="열기",command=open_file)
menu_file.add_command(label="저장",command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기",command=root.quit)
menu.add_cascade(label="파일",menu=menu_file)

# menu_edit=Menu(menu,tearoff=0)
menu.add_cascade(label="편집")

# menu_form=Menu(menu,tearoff=0)
menu.add_cascade(label="서식")

# menu_view=Menu(menu,tearoff=0)
menu.add_cascade(label="보기")

# menu_help=Menu(menu,tearoff=0)
menu.add_cascade(label="도움말")

root.config(menu=menu)  

root.mainloop()
