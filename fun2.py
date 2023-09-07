from fun import AbsFun


class Fun(AbsFun):
    def __init__(self):
        super().__init__()
        self.name = "x*x + y*y"

    def get(self, x, y):
        return x * x + y * y

    def dx(self, x, y):
        return 2 * x

    def dy(self, x, y):
        return 2 * y
