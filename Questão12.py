class MinhaRotina:
    def acordar(self):
        print('Tomar banho para ir para a aula.')

    def cafe_da_manha(self):
        print('Vou comer no ap.')


class RotinaComum:
    def acordar(self):
        print('Estou atrasado para o rancho. Vou sem tomar banho.')

    def cafe_da_manha(self):
        print('Vou comer no rancho. ')


class ExecutaRotina:
    def execute(self, pessoa):
        pessoa.acordar()
        pessoa.cafe_da_manha()


rotina = MinhaRotina()
p = ExecutaRotina()
p.execute(rotina)
