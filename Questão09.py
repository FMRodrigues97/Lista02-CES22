class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type


class Plotter:
    def plot(self, ratio, topleft):
        print(f'Plotting at {topleft}, {ratio}')


class Polygon(Shape, Plotter):
    geometric_type = 'Polígono'


class RegularPolygon(Polygon):
    geometric_type = 'Polígono Regular'

    def __init__(self, side):
        self.side = side


class RegularHexagon(RegularPolygon):
    geometric_type = 'Hexágono Regular'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)


class Square(RegularPolygon):
    geometric_type = 'Quadrado'

    def area(self):
        return self.side * self.side


class TrianguloEquilatero(RegularPolygon):
    geometric_type = 'Triângulo Equilátero'

    def area(self):
        return (3 ** 0.5 * self.side ** 2)/4


class FormaTerreno(Square):
    def mensagem(self):
        return 'Terreno Quadrado'


hexagon = RegularHexagon(10)
print(hexagon.area())
print(hexagon.get_geometric_type())
hexagon.plot(0.8, (75, 77))

print()

square = FormaTerreno(12)
print(square.area())
print(square.get_geometric_type())
square.plot(0.93, (74, 75))
print(square.mensagem())
