class Animal :
    def walk(self,a): #메소드  여기서 self는 나중에 객체 이름을 받기 때문에 하나를 적어주어야 함
        print(a)
    def sound(self, a):
        print(a)

dog = Animal()
Animal.walk(dog,"걷기")  #원형
dog.walk("걷기")  #변형
cat = Animal()
cat.sound("야옹")