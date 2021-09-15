'''
Yield
Yield는 generator 생성자라 볼 수 있다.
iterator와 비슷하다.
range 자료형을 만든 원리로 볼 수 있을 것 같다.
'''


def genNum():
    print("first number")
    yield 1
    print("second number")
    yield 2
    print("third number")
    yield 3


if __name__ == "__main__":    
    genNum()
    print(type(genNum()))
    gen = genNum()
    for i in range(3):
        next(gen)