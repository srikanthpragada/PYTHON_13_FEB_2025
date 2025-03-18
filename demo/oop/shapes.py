import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


class Rect(Shape):
    def __init__(self, x, y, l, w):
        super().__init__(x, y)
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w


class Square(Shape):
    def __init__(self, x, y, s):
        super().__init__(x, y)
        self.s = s

    def area(self):
        return self.s ** 2


c = Circle(10, 20, 15)
print(c.area())