# input
# a = int(input())
# b = int(input())
a=3
b=7

print(type(a))
c= a+b
print(c)
print (a+b)

# print format
print(a,"+",b,"=",a+b)
print(str(a)+"+"+str(b)+"="+str(a+b))
print(f"{a}+{b}={a+b}")

print("안녕하세요.", end=" ")  #자동 엔터가 싫은경우
print("저는 박민성입니다.")

#operator
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}/{b}={a/b}")
print(f"{a}*{b}={a*b}")
print(f"{a}%{b}={a%b}")

# if 문
a = 0
if a>0 :
    print("양수입니다.")
elif a==0 :
    print("0입니다.")
else :
    print("음수입니다.")

#for 문
# range(n,m,p)이면 n<= x < m p는 커지거나 작아짐
for i in range(10,0,-1) :
    print(i)

# while 문
num = 0
while True:
    if num % 2==0 :
        num += 1
        continue #조건을 만족하면 아래있는것 출력 x

    if num > 10:
        break

    print(num)


    num+=1 #num = num + 1

print("End")
print("")

# list  배열
nums = []
nums.append(1)
nums.append(3)
nums.append(13)
nums.append(14)
print(nums)

nums.extend([2,3,4]) #배열 뒤 이어짐
print(nums)

# slicing
print(nums[2:5]) #n:m n =< x <m-1 단 0번째부터
print(nums[2:])
print(nums[:5])
print(nums[:])

print(nums[0])
print(nums[4])

print([7]*10)
print("*"*10)

print(nums)
nums.remove(3) # 앞에있는거 값
print(nums)
del nums[2]  # x번째 값
print(nums)

# nums.sort() >> 정렬
sorted_nums = sorted(nums)

print(nums)
print(sorted_nums)

sorted_nums.reverse() #역순
print(sorted_nums)

print(nums.index(3)) # 몇번째에 있는지 알려줌
print(nums)
# print(nums.pop(3)) # x번째 있는 것을 뽑아내 출력 또는 저장
a = nums.pop(3)
print(nums)
print(a)

nums.append(2)
nums.append(2)
nums.append(3)

print(nums)
print(nums.count(2)) # 개수

print(len(nums)) #전체 개수
print(nums[-1]) #끝에서 1번째

print()

# string
sent = "Hello my name is minseong"
print(sent)

sent = sent.split(' ')
print(sent)

sent = ' '.join(sent)
print(sent)

print(len(sent)) # 띄어쓰기 포함 글자수
print(sent.count("m"))
print(sent.index("e")) #앞에서 부터 몇번째
print(sent.find("e"))

# print(sent.index("E")) 없으면 오류
print(sent.find("E")) # 없으면 -1
print(sent[-1])
print(sent[3:7])

print(sent.upper())
print(sent.lower())

new_sent= '             hello          '
print(new_sent, end = "#")
print()
print(new_sent.strip(), end="#") # 모든 공백
print()
print(new_sent.rstrip(), end="#") # 오른쪽 공백
print()
print(new_sent.lstrip(), end="#") # 왼쪽 공백
print()

sent = sent.replace('i','p')
print(sent)