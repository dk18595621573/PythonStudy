print("apple? True")
fruit = "apple"
print("apple" == fruit)
print("balale" == fruit)
print("Apple".lower() == fruit)

print("=========================")

alien_color = ["green", "yellow", 'red']
alien = alien_color[2]
if("green" == alien):
    print("good! you got 5 score")
elif("yellow" == alien):
    print("good! you got 10 score")
elif("red" == alien):
    print("good! you got 15 score")

print("=========================")

age = 63
if(age < 2):
    print("This man is a baby")
elif(age < 4):
    print("This man is a child")
elif(age < 13):
    print("This man is a children")
elif(age < 20):
    print("This man is a teenager")
elif(age < 65):
    print("This man is a adult")
elif(age > 65):
    print("The old man")

print("=========================")

favorite_fruits = ["apple", "banana", "litchi"]
favorite_fruit = []
if("apple" in favorite_fruits):
    favorite_fruit.append(favorite_fruits[0])
if("banana" in favorite_fruits):
    favorite_fruit.append(favorite_fruits[1])
if("litchi" in favorite_fruits):
    favorite_fruit.append(favorite_fruits[2])
if("aa" in favorite_fruits):
    favorite_fruit.append(favorite_fruits[2])

print(f"You really like {favorite_fruit}!")

print("=========================")

users = ["admin", "Xiaom", "Zhangx", "Tomd", "Huax"]
copy_users = list(user.lower() for user in users)
new_users = ["admin", "Zhang", "Xinzong", "Tomd", "Mont"]
for new_user in new_users:
    if(new_user.lower() in copy_users):
        print(f"user name {new_user} already existed!")
    else:
        print(f"hello {new_user}!")

print("=========================")

numbers = list(range(1, 10))
for number in numbers:
    if(number == 1):
        print("1st")
    elif(number == 2):
        print("2nd")
    elif(number == 3):
        print("3rd")
    else:
        print(f"{number}th")