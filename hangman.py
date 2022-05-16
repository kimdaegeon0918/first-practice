from random import *

def sum():
    s=""
    for i in answer:
        s+=i+" "
    print(s)
words=["apple","banana","orange"]
answer=[]
pick=words[randrange(0,3)]
l=len(pick)
cnt=0
for i in range(1,l+1):
    answer.append("_")
while(l!=cnt):
    # for i in answer:
    #     print(i,end=" ")
    # print("\n")
    sum()
    key=input("Input letter >")

    idx=0
    correct="Wrong"
    for i in pick:
        if i==key:
            correct="Correct"
            answer[idx]=key
            cnt+=1
        idx+=1
    print(correct,"\n")
sum()
print("Succeed")
