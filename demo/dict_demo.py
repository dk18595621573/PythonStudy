man = {"name": "Tom·ding", "age": 23, "address": "上海市宝山区场中路2588弄"}
print(f"name:{man["name"]}")
print(f"age:{man['age']}")
print(f"address:{man['address']}")

print("============================")

number = {"zhang": 8, "gouan": 4, "li": 38, "dai": 9}
for k, v in number.items():
    print(f"{k} love {v}")
for name in number.keys():
    print(f"{name}")

print("============================")

keyword = {"if": "条件判断", "for": "循环指定的值", "list()": "将一个对象转换为 list 列表"}
for k, v in keyword.items():
    print(f"{k}:\n\t{v}")

print("============================")

man_0 = {"name": "Tom·ding", "age": 23, "address": "上海市宝山区场中路2588弄"}
man_1 = {"name": "xiaoMing", "age": 22, "address": "上海市宝山区场中路2588弄"}
man_2 = {"name": "zhangSan", "age": 21, "address": "上海市宝山区场中路2588弄"}
peoples = [man_0, man_1, man_2]
for people in peoples:
    print(f"name:{people["name"]}, age:{people["age"]}, address:{people["address"]}")

print("============================")

pet_0 = {"name": "dog", "master": "wang"}
pet_1 = {"name": "cat", "master": "zhang"}
pet_2 = {"name": "pig", "master": "li"}
pets = [pet_0, pet_1, pet_2]
for pet in pets:
    print(f"name:{pet["name"]}, master:{pet["master"]}")

print("============================")

favorite_place_0 = {"name": "wang", "love": ["Shanghai", "Beijing"]}
favorite_place_1 = {"name": "zhang", "love": ["Chongqing", "Sichuan"]}
favorite_places = [favorite_place_0, favorite_place_1]
for favorite_place in favorite_places:
    print(f"name:{favorite_place["name"]}")
    for love in favorite_place["love"]:
        print(f"love:{love}")