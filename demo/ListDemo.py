# 列表
names = ["张无忌", "孙悟空", "红孩儿"]
print(names)
print(names[0])
message = f"倚天屠龙记主角是：{names[0]}"
print(message)

celebrity = ["达芬奇","爱因斯坦","塔姆·玎","巴拉姆"]
print(f"名人{celebrity[1]}无法赴约")
celebrity[1] = "库克"
print(f"被替换赴约的名人{celebrity[1]}")
message = "赴约的人："
print(f"{message}{celebrity[0]}")
print(f"{message}{celebrity[1]}")
print(f"{message}{celebrity[2]}")
print(f"{message}{celebrity[3]}")

print("======更大的餐桌======")
celebrity.insert(0, "拜登")
celebrity.insert(2, "特朗普")
celebrity.append("黄婆娘")
print(celebrity)

print(len(celebrity))

print("======餐桌无法到达，只能邀请两位======")
print(f"非常抱歉，不能让您参加了：{celebrity.pop()}")
print(f"非常抱歉，不能让您参加了：{celebrity.pop()}")
print(f"非常抱歉，不能让您参加了：{celebrity.pop()}")
print(f"非常抱歉，不能让您参加了：{celebrity.pop()}")
print(f"非常抱歉，不能让您参加了：{celebrity.pop()}")
print(celebrity)
print(f"很高兴您来参加：{celebrity[0]}")
print(f"很高兴您来参加：{celebrity[1]}")
celebrity.clear()
print(celebrity)


print("======旅游城市======")
city = ["Shanghai", "Xizang", "Chengdu", "Dali", "Anhui"]
print(f"旅游城市{city}")
print(f"排序{sorted(city)}")
print(f"原始列表{city}")
print(f"排序{sorted(city, reverse=True)}")
print(f"原始列表{city}")
city.reverse()
print(f"排序{city}")
city.sort()
print(f"排序{city}")
city.sort(reverse=True)
print(f"排序{city}")
# city[100]