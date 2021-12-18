"""
txt 파일 입출력은 Database를 이용하면서 자주 이용하지는 않지만,
기본적으로 알고 있어야 할 요소라는 생각이 든다.
"""

file = open("newfile.txt", "w")

"""
두번째 parameter 값은 파일 열기 모드를 의미하는데,
'r', 'w', 'a' 세가지 종류가 있다.
'r'은 파일을 읽기만 할 때 사용하고
'w'는 파일에 내용을 새로 쓸 때 사용하며
'a'는 파일에 내용을 추가할 때 사용한다.
"""

file.write("Hello World\n")
file.write("Nice to meet you\n")
file.close()

"""
write 함수를 이용하여 글을 작성할 수 있다.
중요한 점은 file을 open 했으면 마지막에는 꼭 close를 해주어야 한다는 점이다.
"""

file = open("newfile.txt", "r")
line = file.readline()
print(line)
lines = file.readlines()
print(lines)
file.close()

"""
readline 함수를 이용하여 한 줄씩 읽어올 수 있고,
readlines 함수를 통하여 모든 줄을 리스트 형태로 읽어올 수 있다.
역시 마지막에는 close 함수를 사용해주어야 한다.
"""
