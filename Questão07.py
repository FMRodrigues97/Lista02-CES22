class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_line_to(self, p2):
        return (self.y - p2.y) / (self.x - p2.x), self.y - self.x * (self.y - p2.y) / (self.x - p2.x)


print(Point(4, 11).get_line_to(Point(6, 15)))
