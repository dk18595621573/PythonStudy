from restaurant.Restaurant import Restaurant
import user.User as u

my_restaurant = Restaurant("夏县小吃", "小吃")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(134)
my_restaurant.describe_restaurant()
my_restaurant.increment_number_served(30)
my_restaurant.describe_restaurant()

lz = Restaurant("兰州拉面", "面")
lz.describe_restaurant()

hg = Restaurant("旋转小火锅", "火锅")
hg.describe_restaurant()

print("==================================")

class IceCreamStand(Restaurant):
    """冰淇淋小店"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["草莓口味冰淇淋", "榴莲口味冰淇淋", "米多奇冰淇淋"]

    def describe_ice_cream_stand(self):
        """打印冰淇淋口味"""
        print("下列冰淇淋:")
        for flavor in self.flavors:
            print(flavor)

my_ice_cream_stand = IceCreamStand("进口冰淇淋", "冰淇淋")
my_ice_cream_stand.describe_ice_cream_stand()

print("==================================")


admin = u.Admin("hei", "xiao")
admin.privileges.show_privileges()

print("==================================")

xiao_ming = u.User("小", "明", age = 23, address = "2588弄")
xiao_ming.greet_user()
xiao_ming.increment_login_attempts()
xiao_ming.increment_login_attempts()
xiao_ming.increment_login_attempts()
xiao_ming.increment_login_attempts()
xiao_ming.describe_user()
xiao_ming.reset_login_attempts()
xiao_ming.describe_user()