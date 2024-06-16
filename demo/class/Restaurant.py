"""餐厅类"""

class Restaurant:
    """餐厅"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """打印信息"""
        print(f"餐厅名称:{self.restaurant_name}, 有{self. number_served}人就餐过")

    def open_restaurant(self):
        """营业"""
        print("餐厅正在营业")

    def set_number_served(self, number_served):
        """设置就餐人数"""
        self.number_served = number_served
    
    def increment_number_served(self, number_served):
        """累计就餐人数"""
        self.number_served += number_served