"""筛子类"""

from random import randint

class Die:
    """筛子"""
    def __init__(self, sides) -> None:
        self.sides = 6

    def roll_die(self):
        """抛掷筛子"""
        print(randint(1, 6))