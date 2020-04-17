class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect_x(self):
        return self.x, -self.y


print(Point(3, 5).reflect_x())
