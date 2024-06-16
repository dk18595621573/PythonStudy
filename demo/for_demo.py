foods = ["烤鱼", "红烧排骨", "西红柿拌面", "东坡肉"]
for food in foods:
    print(f"我喜欢吃：{food}")
print("我非常喜欢吃它们")
friend_foods = foods[:]
foods.append("西葫芦炒肉丝")
friend_foods.append("把子肉")
print(foods)
print(friend_foods)

print("=========================")

zoons = ["狮子", "老虎", "猫"]
for zoon in zoons:
    print(f"{zoon}会成为很棒的宠物")
print("它们都是猫科动物")

print("=========================")

numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)

numbers = []
for number in range(3, 31):
    if(number%3 == 0):
        numbers.append(number)
print(numbers)

numbers = []
for number in range(1, 11):
    numbers.append(number ** 3)
print(numbers)

numbers = list(number ** 3 for number in range(1, 11))
print(numbers)

print("=========================")

print("The first three items in the list are:")
for number in numbers[:3]:
    print(number)
# l = abs()
print("=========================")
for number in numbers[4 : 7]:
    print(number)
print("=========================")
for number in numbers[-3:]:
    print(number)

print("=========================")

self_helps = ("煎蛋", "苹果", "虾", "鱼肉", "豆腐")
for self_help in self_helps:
    print(self_help)
print("=========================")
self_helps = ("煎蛋", "梨", "凉皮", "鱼肉", "豆腐")
for self_help in self_helps:
    print(self_help)