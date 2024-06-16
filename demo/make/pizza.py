"""三明治制作函数"""

def make_food(*materials):
    print("你点的三明治配料如下:")
    for material in materials:
        print(material)