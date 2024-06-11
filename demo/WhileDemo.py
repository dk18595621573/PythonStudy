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

while True:
    number = input("请问年龄多大:")
    number = int(number)
    if number == 0:
        break
    if number < 3:
        print("免费门票")
    elif number < 12:
        print("门票 12 块钱")
    elif number > 12:
        print("门票 15 块钱")
    else:
        print("无法识别退出")
        break