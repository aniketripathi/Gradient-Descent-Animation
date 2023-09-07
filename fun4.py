from fun import AbsFun


class Fun(AbsFun):
    def __init__(self):
        super().__init__()
        self.name = "x**4 + y**4"

    def get(self, x, y):
        return x**4 + y**4

    def dx(self, x, y):
        return 4 * x**3

    def dy(self, x, y):
        return 4 * y**3
