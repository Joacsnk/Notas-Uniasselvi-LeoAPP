from os import system as sy
sy('cls')
while True:
    prova = str(input('\nQual é a nota que você precisa saber?    Discursiva (1)  Final (2): '))
    sy('cls')
    match prova:
        case '2':
            while True:
                pesonota1 = float(input('\33[36mPeso da Avaliação I: '))
                pesonota2 = float(input('Peso da Avaliação II: '))
                pesonota3 = float(input('Peso da Avaliação III (Discursiva): '))
                pesonota4 = float(input('Peso da Avaliação IV (Final): '))
                if pesonota1 + pesonota2 + pesonota3 + pesonota4 == 10:
                    sy('cls')
                    break
                else:
                    sy('cls')
                    print('\n\33[31mERRO. Os valores não são igual a 10 \33[m\n')  
            while True:   
                nota1 = float(input('\n\33[34mNota da Avaliação I: '))
                nota2 = float(input('Nota da Avaliação II: '))
                nota3 = float(input('Nota da Avaliação III (Discursiva): '))
                media = float(((nota1 * pesonota1) + (nota2 * pesonota2) + (nota3 * pesonota3)) / 10)
                if media < 7:
                    sy('cls')
                    print(f'\n\33[mA média das três provas foi de \33[1;31m{media}\33[m')
                    while True:
                        for i in range(1, 11):
                            if (media + (i * pesonota4 / 10)) < 7.00:
                                i += 1
                            else:
                                necessario = (media + (i * pesonota4 / 10))
                                break
                        print(('\33[mVocê precisa de \33[1;32m{:.0f}\33[m na avaliação final para passar'.format(i)))
                        break
                    break
                else:
                    sy('cls')
                    print(f'\n\33[mParabéns, sua média foi \33[32m{media}\33[m e você passou.')
                    break
            break
        case '1':
            while True:
                pesonota1 = float(input('\33[36mPeso da Avaliação I: '))
                pesonota2 = float(input('Peso da Avaliação II: '))
                pesonota3 = float(input('Peso da Avaliação III (Discursiva): '))
                pesonota4 = float(input('Peso da Avaliação IV (Final): '))
                if pesonota1 + pesonota2 + pesonota3 + pesonota4 == 10:
                    sy('cls')
                    break
                else:
                    sy('cls')
                    print('\n\33[31mERRO. Os valores não são igual a 10 \33[m\n')  
            while True:   
                nota1 = float(input('\n\33[34mNota da Avaliação I: '))
                nota2 = float(input('Nota da Avaliação II: '))
                nota4 = float(input('Nota da Avaliação IV (Discursiva): '))
                media = float(((nota1 * pesonota1) + (nota2 * pesonota2) + (nota4 * pesonota4)) / 10)
                if media < 7:
                    sy('cls')
                    print(f'\n\33[mA média das três provas foi de \33[1;31m{media}\33[m')
                    while True:
                        for i in range(1, 11):
                            if (media + (i * pesonota3 / 10)) < 7.00:
                                i += 1
                            else:
                                necessario = (media + (i * pesonota3 / 10))
                                break
                        print(('\33[mVocê precisa de \33[1;32m{:.0f}\33[m na avaliação discursiva para passar'.format(i)))
                        break
                    break
                else:
                    sy('cls')
                    print(f'\n\33[mParabéns, sua média foi \33[32m{media}\33[m e você passou.')
                    break
            break
    print('\n\33[31mERRO 2. Opção inválida \33[m')