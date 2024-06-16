from make.pizza import make_food as mf

mf("洋葱", "大蒜", "辣椒")

def display_message():
    """第一个函数"""
    print("for 循环操作真是无敌")

display_message()

def favorite_book(title):
    """喜欢的书"""
    print(f"我最喜欢的一本书是{title}")

favorite_book("爱丽丝")

def make_shirt(size, title='I Love Python'):
    """制作衬衫"""
    print(f"尺寸:{size}, 文字:{title}")

make_shirt("XXL", "China")
make_shirt(title="China", size="XXL")
make_shirt("XXL")

def describe_city(city, country='China', food=''):
    """城市"""
    city = {"city": {city}, "country":{country}}
    if food:
        city["food"] = food
    return city

name = describe_city("ShangHai")
print(name)
name = describe_city("QiaoBen", "RiBen")
print(name)
name = describe_city("QiaoBen", "RiBen", "小笼包子")
print(name)

print("=======================")


def show_messages(messages):
    for message in messages:
        print(message)

messages = ["Hi", "Hillo", "ok"]
# show_messages(messages)


def send_messages(messages, sent_messages):
    while messages:
        sent_messages.append(messages.pop())

sent_messages = []
send_messages(messages[:], sent_messages)

for sent_message in sent_messages:
    print(sent_message)

for message in messages:
    print(message)

print("=======================")

def make_food(*materials):
    print("你点的三明治配料如下:")
    for material in materials:
        print(material)

make_food("洋葱", "大蒜", "辣椒")

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user = build_profile("zhang", "san", age = 23, address = "2588 弄")
print(user)

def make_car(maker, model, **agrs):
    agrs["maker"] = maker
    agrs["model"] = model
    return agrs

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)