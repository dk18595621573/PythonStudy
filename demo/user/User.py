"""用户类"""

class User:
    def __init__(self, first_name, last_name, **args) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.args = args
        self.login_attempts = 0

    def describe_user(self):
        """打印方法"""
        print(f"姓名:{self.first_name} {self.last_name}, 重试登录次数:{self.login_attempts}, 其他参数:")
        for k, v in self.args.items():
            print(f"{k}, {v}")

    def greet_user(self):
        """问候方法"""
        print(f"你好,{self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        """累计尝试登录次数"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """重置登录次数"""
        self.login_attempts = 0

class Privileges():
    """权限"""
    def __init__(self):
        self.privileges = ["add", "delete", "ban"]

    def show_privileges(self):
        """查看权限"""
        print("权限列表:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    """管理员"""
    def __init__(self, first_name, last_name, **args) -> None:
        super().__init__(first_name, last_name, **args)
        self.privileges = Privileges()