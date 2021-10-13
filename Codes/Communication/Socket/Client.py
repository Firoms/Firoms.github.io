from socket import *
import threading
import time


def send(sock):
    while True:
        msg = input(">>> ")
        sock.send(msg.encode("utf-8"))


def rec(sock):
    while True:
        res = sock.recv(1024)
        print("상대방 : " + res.decode("utf-8"))


clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(("192.168.0.96", 8081))  # 127.0.0.1 은 항상 자신의 아이피
print("서버와 연결되었습니다.")


s = threading.Thread(target=send, args=(clientSock,))
r = threading.Thread(target=rec, args=(clientSock,))
s.start()
r.start()

while True:
    time.sleep(1)
    pass
