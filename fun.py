import numpy as np
from abc import abstractmethod


class AbsFun:
    def __init__(self):
        self.n = 30
        self.xrange = (-10, 10)
        self.xrange = (-10, 10)
        self.init_point = (10, 10)
        self.rate = 1
        self.count = 20
        self.name = "Function Name"

    @abstractmethod
    def get(self, x, y):
        return

    @abstractmethod
    def dx(self, x, y):
        return

    @abstractmethod
    def dy(self, x, y):
        return

    def dlen(self, x, y):
        dx = self.dx(x, y)
        dy = self.dy(x, y)
        return np.sqrt(dx * dx + dy * dy)
