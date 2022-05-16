sum=0
cnt=0
while True:
    k=input()
    if k=="-1":
        break
    else:
        sum+=int(k)
        cnt+=1

print("합계 : {}".format(sum))
print("횟수 : {}".format(cnt))
print("평균 : {}".format(sum/cnt))