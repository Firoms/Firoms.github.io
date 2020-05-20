f = open("note.txt", "w")
f.write("Hello World\n")
f.write("Nice to meet you\n")
f.write("codinglab\n")
f.close()

f = open("note.txt", "r")
s1 = f.readline()
print(s1)
s2 = f.readlines() # 리스트 형태로 반환
print(s2)
f.close()