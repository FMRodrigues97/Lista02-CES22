import math
import abc


class Círculo(object):
    def __init__(self, raio, altura):
        self.raio = raio
        self.altura = altura

    '''Método Abstrato:
        representa uma função que deve ser herdada e implementada nas classes
        filhas, mas ele originalmente não possui corpo na classe mãe. Ou seja, 
        na classe mãe ele é apenas uma assinatura, indicando que cabe às classes
        filhas a definição de como ele deve funcionar.'''
    @abc.abstractmethod
    def sabor(self):
        pass

    '''Método Estático:
        Útil para se fazer operações dentro da classe, como uma função
        de cálculo de área, por exemplo. Você pode ter a classe Circulo e 
        métodos que podem ser chamados sem precisar de instancia, pois o 
        objetivo é o calculo:'''

    @staticmethod
    def calcular_area(raio):
        return math.pi * (raio ** 2)

    '''Método de Classe:
        Pode ser usado diretamente a partir do nome da classe, e não de uma instância'''

    @classmethod
    def calcular_volume(cls, altura, raio):
        return altura * cls.calcular_area(raio)

    def get_volume(self):
        return self.calcular_volume(self.altura, self.raio)


class Pizza(Círculo):
    sabor = 'Quatro Queijos'


pizza = Pizza(3, 2)
print(pizza.get_volume())
print(pizza.sabor)
