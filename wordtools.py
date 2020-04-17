import sys


def cleanword(palavra):
    clean = ''
    for caractere in palavra:
        if caractere.isalpha():
            clean += caractere
    return clean


def has_dashdash(palavra):
    for i in range(0, len(palavra) - 1):
        if palavra[i] == '-' and palavra[i + 1] == '-':
            return True
    return False


def extract_words(frase):
    frase = frase.lower().strip()
    for caractere in frase:
        if not caractere.isalpha():
            frase = frase.replace(caractere, " ")
    palavras = frase.split()
    return palavras


def wordcount(termo, lista_de_palavras):
    contador = 0
    for palavra in lista_de_palavras:
        if palavra == termo:
            contador += 1
    return contador


def wordset(lista_de_palavras):
    lista_de_palavras_unicas = []
    for palavra in lista_de_palavras:
        if palavra not in lista_de_palavras_unicas:
            lista_de_palavras_unicas.append(palavra)
    return sorted(lista_de_palavras_unicas)


def longestword(lista_de_palavras):
    maior = 0
    for palavra in lista_de_palavras:
        if len(palavra) > maior:
            maior = len(palavra)
    return maior


def test(passou):
    linha = sys._getframe(1).f_lineno
    if passou:
        msg = f'Teste na linha {linha} \033[1;32mOK\033[m.'
    else:
        msg = f'Teste na linha {linha} \033[1;31mFALHOU\033[m.'
    print(msg)


def test_suite():
    test(cleanword("what?") == "what")
    test(cleanword("'now!'") == "now")
    test(cleanword("?+='w-o-r-d!,@$()'") == "word")
    print()

    test(has_dashdash("distance--but"))
    test(not has_dashdash("several"))
    test(has_dashdash("spoke--"))
    test(has_dashdash("distance--but"))
    test(not has_dashdash("-yo-yo-"))
    test(has_dashdash("--teste"))
    test(has_dashdash("teste--"))
    test(not has_dashdash("-teste-"))
    print()

    test(extract_words("Now is the time! 'Now', is the time? Yes, now.") == ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now'])
    test(extract_words("she tried to curtsey as she spoke--fancy") == ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy'])
    test(extract_words("--frase--teste--") == ['frase', 'teste'])
    test(extract_words("     ---     ---    mais - um 65646 teste 88686") == ['mais', 'um', 'teste'])
    print()

    test(wordcount("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2)
    test(wordcount("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3)
    test(wordcount("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
    test(wordcount("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)
    print()

    test(wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
    test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
    test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["a", "am", "are", "be", "but", "is", "or"])
    print()

    test(longestword(["a", "apple", "pear", "grape"]) == 5)
    test(longestword(["a", "am", "I", "be"]) == 2)
    test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
    test(longestword([ ]) == 0)
    print()


test_suite()
