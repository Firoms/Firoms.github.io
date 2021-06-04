'''
threading 모듈은 동시성을 이용할 수 있게 해주는 모듈이다.
사실 동시라기보단 빠르게 번갈아 작업하는 형식인데,
직접 이용해본 결과, threading은 예측 불가한다는 생각이 들었다.
'''

import threading

def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print("Subthread", total)


t = threading.Thread(target=sum, args=(1, 100000))
t.start()

print("Main Thread")
