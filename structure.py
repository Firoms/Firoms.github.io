# class Structure:
#     def __init__(self, height, space):
#         self.height = height
#         self.space = space
#
#     def describe(self):
#         print(f"이 건물의 높이는 {self.height}층이고 넓이는 {self.space}평 입니다.")
# s1 = Structure(20, 30)
# s1.describe()
#
# class SoccerField(Structure):
#     def __init__(self, height, space, seats):
#         super().__init__(height,space)
#         self.seats = seats
#     def describe(self):
#         super().describe()
#         print(f"좌석수는 {self.seats}개 입니다.")
#
# soccer = SoccerField(3, 400, 50000)
# soccer.describe()
import json

class Item:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
    def describe(self):
        print(f"Name  = {self.name}")
        print(f"Weight  = {self.weight}")
        print(f"Price  = {self.price}")

items = []
class Weapon(Item):
    def __init__(self, name, weight, price, damage):
        super().__init__(name, weight, price)
        self.damage = damage
        self.dic = {}
    def describe(self):
        super().describe()
        print(f"Damage  = {self.damage}")
    def save(self):
        self.dic['Name'] = self.name
        self.dic['Weight'] = self.weight
        self.dic['Price'] = self.price
        self.dic['Damage'] = self.damage
        items.append(self.dic)

class Armor(Item):
    def __init__(self, name, weight, price, defence):
        super().__init__(name, weight, price)
        self.defence = defence
        self.dic = {}
    def describe(self):
        super().describe()
        print(f"Defence  = {self.defence}")
    def save(self):
        self.dic['Name'] = self.name
        self.dic['Weight'] = self.weight
        self.dic['Price'] = self.price
        self.dic['Defence'] = self.defence



sword = Weapon("sword", 20.0, 3000, 15)
gun = Weapon("gun", 304, 123, 22)
bomb = Weapon("bomb", 121, 20.12, 0.9)
sword.save()
gun.save()
bomb.save()
print(items)
B = open("Weapon.txt", "w")
B.write(str(json.dumps(items)))
B.close()



# shield = Armor("shield", 25.3, 3500, 30)
# shield.save()
# shield2 = Armor("shield2", 1255.3, 332460, 31242)
# shield2.save()
# sword.describe()
# shield.describe()
#
#
# item1 = Item("test", "19", 350)
# item1.describe()
#
# item2 = Item("atk", "1", 100)
# item3 = Item("dfd", "8", 150)