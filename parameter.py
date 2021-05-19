'''
입력되는 매개변수(parameter)의 개수를 지정하고 싶지 않을 때
asterisk(*)을 사용하여 인자 값을 받을 수 있다.
보통 arguments의 줄임말인 args라고 입력받는다.
'''

def add(*args):
    total = 0
    for i in args:
        total += i
    return total


result1 = add(1,2,3,4,5)
print(result1)


'''
asterisk(*)를 두개 사용하게 되면 dictionary 형식으로 인자 값을 받을 수 있다.
역시 매개변수의 개수를 지정하고 싶지 않을 때 사용한다.
보통 keyword arguments의 줄임말인 kwarg라고 입력받는다.
'''

def num(**kwargs):
    return kwargs 

result2 = num(one=1, two=2, three=3)
print(result2)