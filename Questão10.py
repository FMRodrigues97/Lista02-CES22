def letras_maiusculas(função):
    def maiuscula():
        return função().upper()

    return maiuscula


@letras_maiusculas  # Decorator
def meu_nome():
    return 'Fernando'


nome = meu_nome()
print(nome)
