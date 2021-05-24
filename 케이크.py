
class Cake:
    def __init__(self, name, price, ingredient):
        self.name = name
        self.price = price
        self.ingredient = ingredient


class Shop:
    def __init__(self):
        self.ingredient = {}
        self.product = {}

    def buy_ingredient(self, buy_dict):
        for keys, values in buy_dict.items():
            if keys in self.ingredient.keys():
                self.ingredient[keys] += values
            else:
                self.ingredient[keys] = values

    def current_ingredient(self):
        print("현재 보유한 재료는", end=" ")
        for keys, values in self.ingredient.items():
            print(f", {keys} ({values}개)", end="")
        print("입니다.")

    def make_cake(self, cake):
        for keys, values in cake.ingredient.items():
            if keys in self.ingredient.keys():
                if values <= self.ingredient[keys]:
                    pass
                else:
                    need = values - self.ingredient[keys]
                    return print(f"{keys} 재료 {need}개가 부족합니다.")
            else:
                return print(f"{keys} 재료 {values}개가 부족합니다.")
        for keys, values in cake.ingredient.items():
            self.ingredient[keys] -= values
            if self.ingredient[keys] == 0:
                del self.ingredient[keys]
        print(f"{cake.name} 1개 완성!")
        if cake in self.product.keys():
            self.product[cake] += 1
        else:
            self.product[cake] = 1


class Pos:
    def __init__(self, cake_shop):
        self.cake_shop = cake_shop
        self.money = 0

    def current_cakes(self):
        print("현재 재고는")
        for keys, values in cake_shop.product.items():
            print(f"{keys.name} : {values} ")

    def sell_cake(self, cakename):

        for cake in self.cake_shop.product.keys():
            if cake.name == cakename:
                if cakename in [x.name for x in cake_shop.product.keys()]:
                    cake_shop.product[cake] -= 1
                    print(
                        f"{cakename} 판매완료. 현재 남은 {cakename}의 개수는 {cake_shop.product[cake]}개 입니다."
                    )
                    if cake_shop.product[cake] == 0:
                        del cake_shop.product[cake]
                    self.money += cake.price
                    return

        print(f"{cakename} 재고가 없습니다.")


cheesecake = Cake("Cheese Cake", 6900, {"cheese": 2, "egg": 2, "butter": 2})
chococake = Cake("Chocolate Cake", 5900, {"chocolate": 2, "egg": 2, "butter": 2})
carrotcake = Cake(
    "Carrot Cake", 5500, {"carrot": 2, "walnut": 2, "egg": 1, "butter": 1}
)
creamcake = Cake("Fresh Cream Cake", 4500, {"cream": 3, "egg": 1, "butter": 1})
swpotatocake = Cake(
    "Sweet Potato Cake", 6500, {"sweet potato": 3, "egg": 2, "butter": 1}
)

cake_shop = Shop()
cake_shop.buy_ingredient(
    {"cheese": 5, "carrot": 3, "sweet potato": 3, "egg": 10, "butter": 10}
)
cake_shop.current_ingredient()
cake_shop.buy_ingredient({"chocolate": 3, "walnut": 2, "egg": 12, "butter": 12})
cake_shop.current_ingredient()

print("\nMAKE CAKE")
cake_shop.make_cake(creamcake)
print(cake_shop.ingredient)
cake_shop.make_cake(carrotcake)
print(cake_shop.ingredient)
cake_shop.make_cake(carrotcake)
print(cake_shop.ingredient)
cake_shop.make_cake(cheesecake)
print(cake_shop.ingredient)
cake_shop.make_cake(cheesecake)
print(cake_shop.ingredient)
cake_shop.make_cake(chococake)
print(cake_shop.ingredient)
cake_shop.make_cake(swpotatocake)
print(cake_shop.ingredient)
cake_shop.current_ingredient()

pos = Pos(cake_shop)
print()
pos.current_cakes()

print()
pos.sell_cake("Cheese Cake")
pos.current_cakes()

print()
pos.sell_cake("Cheese Cake")
pos.current_cakes()

print()
pos.sell_cake("Cheese Cake")

print()
print(pos.money)
