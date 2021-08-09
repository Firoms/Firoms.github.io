# I번 - 고장난 계산기 (Calculator) 게임
import sys
N, Q = map(int, sys.stdin.readline().split())
text = sys.stdin.readline().rstrip()
newText = "*"
for i in text:
    if i=="+" or i=="*":
        if newText[-1]=="" or newText[-1]=="+" or newText[-1]=="*":
            pass
        else:
            newText += i
    else:
        newText += i
if newText[-1]=="+" or newText[-1]=="*":
    newText = newText[:-1]
newText = newText[1:]

if newText=="":
    print(-1)
else:
    print(eval(newText))


for i in range(Q):
    l, r, x = map(int, sys.stdin.readline().split())
    newText = "*"
    nextTime = ""
    zeroCheck = 0
    for idx, i in enumerate(text):
        if i=="+":
            i = "10"
        if i=="*":
            i = "11"
        if l-1<=idx<=r-1:
            i = str((int(i) + x)%12)
        if i=="10":
            i="+"
        if i=="11":
            i="*"
        nextTime += i
        if i=="+" or i=="*" or i=="0":
            if newText[-1]=="" or newText[-1]=="+" or newText[-1]=="*":
                pass
            else:
                newText += i
        else:
            newText += i
        if i=="0":
            zeroCheck+=1

    if newText[-1]=="+" or newText[-1]=="*":
        newText = newText[:-1]
    newText = newText[1:]

    if newText=="" and zeroCheck>0:
        print(0)
        nextTime ="0"*zeroCheck
    elif newText=="":
        print(-1)
    else:
        print(eval(newText))
    text = nextTime