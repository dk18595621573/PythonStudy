import os
import json

number_json_file_name = os.getcwd() + "/demo/io/file/number.json"

try:
    with open(number_json_file_name) as f:
        print(json.load(f));
except FileNotFoundError:
    number = input("请输入你喜欢的数:")
    with open(number_json_file_name, "w") as f:
        json.dump(int(number), f)


