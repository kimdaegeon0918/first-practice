from tkinter import *

root=Tk()
root.title("Nado GuI")
root.geometry("640x480")

chkbar=IntVar()
chkbox=Checkbutton(root,text="오늘하루보지않기",variable=chkbar)
# chkbox.select()
# chkbox.deselect()

chkbox.pack()

chkbar2=IntVar()
chkbox2=Checkbutton(root,text="일주일동안보지않기",variable=chkbar2)
chkbox2.pack()

def btncmd():
    print(chkbar.get()) 
    print(chkbar2.get()) 

btn=Button(root,text="클릭",command=btncmd)
btn.pack()
root.mainloop()
