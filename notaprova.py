escolhadenota = int(input('\nQual é a nota que você precisa saber?    Discursiva (1)  Final (2): '))
if escolhadenota == 2:
    x = False
    i = 1
    pesonota1 = float(input('\33[36mPeso da Avaliação I: '))
    pesonota2 = float(input('Peso da Avaliação II: '))
    pesonota3 = float(input('Peso da Avaliação III (Discursiva): '))
    pesonota4 = float(input('Peso da Avaliação IV (Final): '))
    if pesonota1 + pesonota2 + pesonota3 + pesonota4 == 10:
        nota1 = float(input('\n\33[34mNota da Avaliação I: '))
        nota2 = float(input('Nota da Avaliação II: '))
        nota3 = float(input('Nota da Avaliação III (Discursiva): '))
        media = float(((nota1 * pesonota1) + (nota2 * pesonota2) + (nota3 * pesonota3)) / 10)
        if media < 7:
            print(f'\n\33[mA média das três provas foi de \33[1;31m{media}\33[m')
            while x == False:
                if (media + (i * pesonota4 / 10)) < 7.00:
                    i += 1
                else:
                    necessario = (media + (i * pesonota4 / 10))
                    x = True
            print(('\33[mVocê precisa de \33[1;32m{:.0f}\33[m na avaliação final para passar'.format(i)))
        else:
            print(f'\n\33[mParabéns, sua média foi \33[32m{media}\33[m e você passou.')
    else:
        print('\n\33[31mERRO 1. Os valores não dão 10 \33[m')
elif escolhadenota == 1:
    x = False
    i = 1
    pesonota1 = float(input('\33[36mPeso da Avaliação I: '))
    pesonota2 = float(input('Peso da Avaliação II: '))
    pesonota3 = float(input('Peso da Avaliação III (Discursiva): '))
    pesonota4 = float(input('Peso da Avaliação IV (Final): '))
    if pesonota1 + pesonota2 + pesonota3 + pesonota4 == 10:
        nota1 = float(input('\n\33[34mNota da Avaliação I: '))
        nota2 = float(input('Nota da Avaliação II: '))
        nota4 = float(input('Nota da Avaliação IV (Final): '))
        media = float(((nota1 * pesonota1) + (nota2 * pesonota2) + (nota4 * pesonota4)) / 10)
        if media < 7:
            print(f'\n\33[mA média das três provas foi de \33[1;31m{media}\33[m')
            while x == False:
                if (media + (i * pesonota3 / 10)) < 7.00:
                    i += 1
                else:
                    necessario = (media + (i * pesonota3 / 10))
                    x = True
            print(('\33[mVocê precisa de \33[1;32m{:.0f}\33[m na avaliação discursiva para passar'.format(i)))
        else:
            print(f'\n\33[mParabéns, sua média foi \33[32m{media}\33[m e você passou.')
    else:
        print('\n\33[31mERRO 1. Os valores não dão 10 \33[m')
else:
    print('\n\33[31mERRO 2. Opção inválida \33[m')