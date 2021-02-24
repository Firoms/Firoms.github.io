import json
from structure import Weapon

# f = open("practice.json", "r")
#
# json_data = json.load(f)
#
# print(json_data["json_string"])
# print(json_data["json_number"])
# print(json_data["json_array"])
# print(json_data["json_object"])
# print(json_data["json_bool"])


weapon = open("Weapon.txt", "r")
weapon_data = json.load(weapon)
for i in weapon_data:

    k = Weapon(i["Name"], i["Weight"], i["Price"], i["Damage"])
    k.describe()
