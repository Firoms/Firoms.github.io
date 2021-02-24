class Marine:

    atkmax = 0
    dfmax = 0
    atk = 5
    df = 0

    def __init__(self):
        self.hp = 40

    def steampack(self):
        if self.hp > 10:
            self.hp -= 10
        else:
            print("스팀팩을 사용할 수 없습니다.")
        print("현재 체력 :", self.hp)

    def atkup(self):
        if Marine.atkmax > 2:
            print("더 이상 공격력을 올릴 수 없습니다.")
        else:
            Marine.atk += 1
            Marine.atkmax += 1
        print(Marine.atk)

    def dfup(self):
        if Marine.dfmax > 2:
            print("더 이상 방어력을 올릴 수 없습니다.")
        else:
            Marine.df += 1
            Marine.dfmax += 1
        print(Marine.df)


class Jimraner(Marine):
    Marine.atk = 7
    Marine.df = 1

    def __init__(self):
        self.hp = 60

    def cloak(self):
        print("클록킹을 활성화합니다.")

    def steampack(self):
        # super().asd() # 원래 asd 코드 까지도 가져올 수 있음 super() 은 자신의 부모 클래스를 의미한다고 생각하면 됨
        if self.hp > 9:
            self.hp -= 9
        else:
            print("스팀팩을 사용할 수 없습니다.")
        print("현재 체력 :", self.hp)


raner1 = Jimraner()
raner2 = Jimraner()
raner1.steampack()
raner1.steampack()
raner1.steampack()
raner1.steampack()
raner1.steampack()
raner1.steampack()
raner1.steampack()
raner1.steampack()
raner1.cloak()
raner2.steampack()
raner2.steampack()
raner1.atkup()
raner1.atkup()
raner1.dfup()
raner2.dfup()
raner2.dfup()
print(raner1.atk, raner2.atk)
print(raner1.df, raner2.df)
