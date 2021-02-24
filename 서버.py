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


serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(("", 8081))
print("서버가 켜졌습니다.")
serverSock.listen(1)

clientSock, addr = serverSock.accept()

print("연결되었습니다.")
s = threading.Thread(target=send, args=(clientSock,))
r = threading.Thread(target=rec, args=(clientSock,))
s.start()
r.start()

while True:
    time.sleep(1)
    pass
