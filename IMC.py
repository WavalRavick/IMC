cont = 0
while True:
    nome = input('Digite o seu Nome? ')
    cont += 1

    if not nome.isalpha():
        print('Digite um Nome Válido.')
        print('')
    else:

        idade = input('Qual a sua Idade: ')
        if not idade.isdigit():
            print('Digite uma Idade Válida.')
            print('')
        else:
            idade = int(idade)

            peso = input('Qual o seu Peso: ')
            if not peso.isdigit():
                print('Digite um Peso Válido.')
                print('')
            else:
                peso = int(peso)

                altura = input('Digite sua Altura Em Centímetros: ')
                if not altura.isdigit():
                    print('Digite uma Altura Válida.')
                    print('')
                else:
                    altura = int(altura)
                    altura = altura / 100

                    IMC = (peso / (altura * altura))  # peso / (altura ** 2)
                    print(f'seu IMC é: {IMC} ')

                    normal = 24.9
                    normal_2 = 18.5
                    obeso = 30.0

                    Intervalo = (normal - normal_2)
                    imc = IMC - normal_2
                    imc_1 = normal - IMC
                    media_Magresa = 100 - ((imc/Intervalo)*100)
                    media_sobrepeso = 100 - media_Magresa

                    Intervalo_2 = (obeso - normal)
                    imc_3 = IMC - normal
                    imc_4 = obeso - IMC
                    media_sobrepeso_2 = 100 - ((imc_3/Intervalo_2)*100)
                    media_obeso = 100 - media_sobrepeso_2

                    print(f'O seu IMC está:')
                    if IMC == normal_2 or IMC <= normal:
                        print("NORMAL")
                        print(f'Você está {media_Magresa:.2f}% da Magresa e à {media_sobrepeso:.2f}% de ser Sobrepeso')
                        break
                    elif IMC < normal_2:
                        print("MAGRESA")
                        break
                    elif IMC > normal < IMC < obeso:
                        print("SOBREPESO")
                        print(f'Você está {media_sobrepeso_2:.2f}% da Normalidade e à {media_obeso:.2f}% da Obesidade')
                        break
                    elif IMC >= obeso:
                        print("OBESO")
                        break
    if not cont == 3:
        continue

    if cont == 3:
        sair = input('Deseja sair? \nDigite [s] para sim e [n] para não: ')
        if sair == 's':
            print('')
            print('Fim!')
            break
        else:
            cont = 0
            print('')
            continue
