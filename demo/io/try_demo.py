import os

number_a = input("请输入一个数字:")
number_b = input("请输入一个数字:")

try:
    number_a = int(number_a)
    number_b = int(number_b)
except ValueError:
    print("输入的不是数字")
else:
    print(f"相加结果={number_a + number_b}")

current_directory = os.getcwd()
cats_file_name = current_directory + "/demo/io/file/test.txt"
dogs_file_name = current_directory +  "/demo/io/file/dogs.txt"
try:
    with open(cats_file_name, "w") as f:
        f.write("test")
    with open(dogs_file_name) as f:
        print(f.read())
except FileNotFoundError:
    print("写入文件出现异常")