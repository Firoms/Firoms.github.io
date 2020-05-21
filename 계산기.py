fst = int(input("첫번째수를 입력하세요. "))
cal = input("연산자를 입력하세요. ")
snd = int(input("두번째수를 입력하세요. "))

class Calculator:

    def __init__(self,a,b):
        #생성자 >> 호출될때 값을 처음부터 집어넣어야함  (단, 최초한번만 되므로 똑같은게 필요할 수도 있음)
        self.a = a
        self.b = b
    def __str__(self): #str 은 인스턴스를 print했을때 return 한 문자를 출력한다.
        return "asdfsadf"
    def setdata(self,a,b):
        self.a = a
        self.b = b
    def add(self) :
        return self.a + self.b
    def sub(self) :
        return self.a - self.b
    def mul(self) :
        return self.a * self.b
    def div(self) :
        return self.a / self.b

class SafeCal(Calculator):
    def div(self):
        if self.b == 0:
            return 0
        else:
            return self.a / self.b

Calc = Calculator(fst,snd)

if cal == '+':
    print(fst, "+", snd, "=", Calc.add())
elif cal == '-':
    print(fst, "-", snd, "=", Calc.sub())
elif cal == '*':
    print(fst, "*", snd, "=", Calc.mul())
elif cal == '/':
    print(fst, "/", snd, "=", Calc.div())
else:
    print("연산자가 잘못되었습니다.")
