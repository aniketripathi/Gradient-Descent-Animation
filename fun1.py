from fun import AbsFun
import numpy as np


class Fun(AbsFun):
    def __init__(self):
        super().__init__()
        self.xrange = (-15, 6)
        self.yrange = (-10, 6)
        self.init_point = (6, 6)
        self.n = 30
        self.name = "e^x + e^y - 2*x*x - 2*y*y"

    # f = e^x + e^y - x*x - y*y
    def get(self, x, y):
        return np.exp(x) + np.exp(y) - 2 * x * x - 2 * y * y

    def dx(self, x, y):
        return np.exp(x) - 4 * x

    def dy(self, x, y):
        return np.exp(y) - 4 * y
