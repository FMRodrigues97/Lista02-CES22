class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def slope_from_origin(self):
        return self.y / self.x
    # O método dará problema quando a coordenada x for zero, ou seja, quando a reta foi vertical.


print(Point(4, 10).slope_from_origin())
