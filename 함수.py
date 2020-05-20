# 매개변수
# 인수


# def add(num1, num2) : #num 1,2 가 매개변수임
#     result = num1 + num2
#     return result   #반환하는 것 / 없어도 됨(안에서 print를 해줘도 되기 때문)
# print(add(1,2))


def add(*args) : #*를 붙여 여러 개를 저장할 수 있음

    '''a = 0
    total = 0
    while a < len(args):
        total += args[a]
        a += 1
    return total'''

    '''total = 0
    for i in range(len(args)):
        total += args[i]
    return total '''

    total = 0
    for i in args :
        total += i
    return total

print(add(1, 2, 3, 4, 5))


# () tuple >> 바꿀 수 없는 값

def add(**kwargs):  #dictionary 로 값을 받음
    print(kwargs)
add(one=1, two=2)

