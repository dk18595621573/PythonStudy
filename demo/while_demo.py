# message = input("请问您要租赁什么汽车:")
# print(message)

print("============================")

# number = input("请问有多少人用餐:")
# number = int(number)
# if number > 8:
#     print("人数太多,没有座位")
# else:
#     print("请用餐")

# flag = ""
# while flag != "quit":
#     flag = input("请问添加什么配料:")
#     if flag != "quit":
#         print(f"配料{flag}添加成功")

# while True:
#     number = input("请问年龄多大:")
#     number = int(number)
#     if number == 0:
#         break
#     if number < 3:
#         print("免费门票")
#     elif number < 12:
#         print("门票 12 块钱")
#     elif number > 12:
#         print("门票 15 块钱")
#     else:
#         print("无法识别退出")
#         break

sandwich_orders = ["西红柿三明治", "五香烟熏牛肉", "芝士三明治", "五香烟熏牛肉", "黄瓜三明治", "五香烟熏牛肉"]
# finished_sandwiches = []
# while sandwich_orders:
#     sandwich_order = sandwich_orders.pop()
#     finished_sandwiches.append(sandwich_order)
# for finished_sandwiche in finished_sandwiches:
#     print(f"I made your {finished_sandwiche}")

print("五香烟熏牛肉卖完了")
for sandwich_order in sandwich_orders:
    if "五香烟熏牛肉" == sandwich_order:
        sandwich_orders.remove(sandwich_order)

for sandwich_order in sandwich_orders:
    print(sandwich_order)

# 旅游城市
citys = {}
flag = True
while flag:
    name = input("你的名字:")
    city = input("你喜欢去的城市:")
    citys[name] = city
    finish = input("还要继续填写么(yes/no):")
    if "no" == finish:
        break
for k, v in citys.items():
    print(f"名称:{k}, 喜欢去的城市:{v}")