"""IO读取写入"""

import os

current_directory = os.getcwd()
print(f"当前工作目录是: {current_directory}")

file_name = current_directory + "/demo/io/file/learning_python.txt"
with open(file_name) as file_object:
    print(file_object.read())

print("=============================")

with open(file_name) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

print("=============================")

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace("Python", "Java").rstrip())

print("=============================")

file_name = current_directory + "/demo/io/file/guest.txt"
with open(file_name, "w") as file_object:
    while True:
        user_name = input("请输入用户名:")
        if "1" == user_name:
            break
        file_object.write(user_name + "\n")
        print(f"您好, {user_name}")