nota_20_caixa = 2
nota_10_caixa = 3
nota_5_caixa = 4
nota_2_caixa = 5
moeda_1_caixa = 5
moeda_50_caixa = 5
moeda_25_caixa = 5
moeda_10_caixa = 10
moeda_5_caixa = 10
run_program = 1
estoque_lata_coca = 5

while run_program == 1:

    print("Deseja acessar o modo de consumidor ou admin?")
    modo = int(input("Para acessar o modo consumidor, digite 1, já para o modo Admin, digite 2: "))
    if modo != 1 and modo != 2:
        while modo != 1 and modo != 2:
            modo = int(input("Para acessar o modo consumidor, digite 1, ja para o modo Admin, digite 2: "))
            print(modo != 1 and modo != 2)
    if modo == 1:
        print(
            '\nMÁQUINA DE REFRIGERANTE \n--------------------------------- \n(1) Coca-Cola 350ml - R$5,00 \n(2) RedBull 350ml - R$8,00 \n(3) Agua sem gas 500ml - R$3,50 \n---------------------------------')

        bebida = int(input("\nEscolha sua bebida (1|2|3): "))
        while bebida != 1 and bebida != 2 and bebida != 3:
            print("\nValor invalido, favor escolher uma das 3 opções!")
            bebida = int(input("Escolha sua bebida (1|2|3)"))

        if bebida == 1:
            custo_bebida = 5
        elif bebida == 2:
            custo_bebida = 8
        else:
            custo_bebida = 3.50

        saldo_inserido = 0
        nota_20_inserida = 0
        nota_10_inserida = 0
        nota_5_inserida = 0
        nota_2_inserida = 0
        moeda_1_inserida = 0
        moeda_50_inserida = 0
        moeda_25_inserida = 0
        moeda_10_inserida = 0
        moeda_5_inserida = 0
        contador_nota_10 = 0
        contador_nota_5 = 0
        contador_nota_2 = 0
        contador_moeda_1 = 0
        contador_moeda_50 = 0
        contador_moeda_25 = 0
        contador_moeda_10 = 0
        contador_moeda_5 = 0

        while saldo_inserido < custo_bebida:
            print(
                f"\nFavor inserir saldo via moedas ou cédulas\nSaldo atual: {saldo_inserido} reais\nCusto da bebida: {custo_bebida} reais")
            print('Para inserir: \n20 reais (1)\n10 reais (2)\n5 reais (3)\n2 reais (4)\n1 real (5)\n50 centavos (6)\n25 centavos (7)\n10 centavos (8)\n5 centavos (9)\n')
            valor_inserido = int(input('Insira o número: '))
            while valor_inserido < 0 or valor_inserido > 9:
                print("\nValor invalido, favor escolher uma das 9 opções!")
                print(
                    'Para inserir: \n20 reais (1)\n10 reais (2)\n5 reais (3)\n2 reais (4)\n1 real (5)\n50 centavos (6)\n25 centavos (7)\n10 centavos (8)\n5 centavos (9)\n')
                valor_inserido = int(input('Insira o número: '))

            if valor_inserido == 1:
                saldo_inserido += 20
                print(f"\nSaldo atual: {saldo_inserido} reais")
                nota_20_inserida += 1

            elif valor_inserido == 2:
                saldo_inserido += 10
                print(f"\nSaldo atual: {saldo_inserido} reais")
                nota_10_inserida += 1

            elif valor_inserido == 3:
                saldo_inserido += 5
                print(f"\nSaldo atual: {saldo_inserido} reais")
                nota_5_inserida += 1

            elif valor_inserido == 4:
                saldo_inserido += 2
                print(f"\nSaldo atual: {saldo_inserido} reais")
                nota_2_inserida += 1

            elif valor_inserido == 5:
                saldo_inserido += 1
                print(f"\nSaldo atual: {saldo_inserido} reais")
                moeda_1_inserida += 1

            elif valor_inserido == 6:
                saldo_inserido += 0.50
                print(f"\nSaldo atual: {saldo_inserido} reais")
                moeda_50_inserida += 1

            elif valor_inserido == 7:
                saldo_inserido += 0.25
                print(f"\nSaldo atual: {saldo_inserido} reais")
                moeda_25_inserida += 1

            elif valor_inserido == 8:
                saldo_inserido += 0.10
                print(f"\nSaldo atual: {saldo_inserido} reais")
                moeda_10_inserida += 1

            elif valor_inserido == 9:
                saldo_inserido += 0.05
                print(f"\nSaldo atual: {saldo_inserido} reais")
                moeda_5_inserida += 1

            if saldo_inserido > custo_bebida:
                troco = saldo_inserido - custo_bebida
                print(f"Seu troco sera de {troco} reais\n")

        while troco > 0:
            while troco >= 10 and nota_10_caixa > 0 or troco >= 10 and nota_10_inserida > 0:
                if nota_10_inserida > 0:
                    troco = troco - 10
                    nota_10_inserida -= 1
                    contador_nota_10 += 1
                    print('Devolvendo uma nota de 10')
                else:
                    troco = troco - 10
                    nota_10_caixa -= 1
                    contador_nota_10 += 1
                    print('Devolvendo uma nota de 10')

            while troco >= 5 and nota_5_caixa > 0 or troco >= 5 and nota_5_inserida > 0:
                if nota_5_inserida > 0:
                    troco = troco - 5
                    nota_5_inserida -= 1
                    contador_nota_5 += 1
                    print('Devolvendo uma nota de 5')
                else:
                    troco = troco - 5
                    nota_5_caixa -= 1
                    contador_nota_5 += 1
                    print('Devolvendo uma nota de 5')

            while troco >= 2 and nota_2_caixa > 0 or troco >= 2 and nota_2_inserida > 0:
                if nota_2_inserida > 0:
                    troco = troco - 2
                    nota_2_inserida -= 1
                    contador_nota_2 += 1
                    print('Devolvendo uma nota de 2')
                else:
                    troco = troco - 2
                    nota_2_caixa -= 1
                    contador_nota_2 += 1
                    print('Devolvendo uma nota de 2')

            while troco >= 1 and moeda_1_caixa > 0 or troco >= 1 and moeda_1_inserida > 0:
                if moeda_1_inserida > 0:
                    troco = troco - 1
                    moeda_1_inserida -= 1
                    contador_moeda_1 += 1
                    print('Devolvendo uma moeda de 1 real')
                else:
                    troco = troco - 1
                    moeda_1_caixa -= 1
                    contador_moeda_1 += 1
                    print('Devolvendo uma moeda de 1 real')

            while troco >= 0.50 and moeda_50_caixa > 0 or troco >= 0.50 and moeda_50_inserida > 0:
                if moeda_50_inserida > 0:
                    troco = troco - 0.50
                    moeda_50_inserida -= 1
                    contador_moeda_50 += 1
                    print('Devolvendo uma moeda de 50 centavos')
                else:
                    troco = troco - 0.50
                    moeda_50_caixa -= 1
                    contador_moeda_50 += 1
                    print('Devolvendo uma moeda de 50 centavos')

            while troco >= 0.25 and moeda_25_caixa > 0 or troco >= 0.25 and moeda_25_inserida > 0:
                if moeda_25_inserida > 0:
                    troco = troco - 0.25
                    moeda_25_inserida -= 1
                    contador_moeda_25 += 1
                    print('Devolvendo uma moeda de 25 centavos')
                else:
                    troco = troco - 0.25
                    moeda_25_caixa -= 1
                    contador_moeda_25 += 1
                    print('Devolvendo uma moeda de 25 centavos')

            while troco >= 0.10 and moeda_10_caixa > 0 or troco >= 0.10 and moeda_10_inserida > 0:
                if moeda_10_inserida > 0:
                    troco = troco - 0.10
                    moeda_10_inserida -= 1
                    contador_moeda_10 += 1
                    print('Devolvendo uma moeda de 10 centavos')
                else:
                    troco = troco - 0.10
                    moeda_10_caixa -= 1
                    contador_moeda_10 += 1
                    print('Devolvendo uma moeda de 10 centavos')

            nota_20_caixa += nota_20_inserida
            nota_10_caixa += nota_10_inserida
            nota_5_caixa += nota_5_inserida
            nota_2_caixa += nota_2_inserida
            moeda_1_caixa += moeda_1_inserida
            moeda_50_caixa += moeda_50_inserida
            moeda_25_caixa += moeda_25_inserida
            moeda_10_caixa += moeda_10_inserida
            moeda_5_caixa += moeda_5_inserida

            print('\nLiberando o produto!')
            print('Obrigado por comprar com a gente!\n')

        continuar = int(input('Deseja continuar com o programa? SIM(1) ou NÃO(2): '))
        if continuar == 2:
            run_program = 0
    else:
        print('\n--------------------------------- \nSeja Bem-vindo ao modo Admin\n')
        print(
            f'Aqui segue o numero de moedas e cédulas de cada tipo:\nCédulas de 20 reais: {nota_20_caixa}\nCédulas de 10 reais: {nota_10_caixa}\nCédulas de 5 reais: {nota_5_caixa}\nCédulas de 2 reais: {nota_2_caixa}\nMoedas de 1 real: {moeda_1_caixa}\nMoedas de 50 centavos: {moeda_50_caixa}\nMoedas de 25 centavos: {moeda_25_caixa}\nMoedas de 10 centavos: {moeda_10_caixa}\nMoedas de 5 centavos: {moeda_5_caixa}')
        valor_total_caixa = (nota_20_caixa * 20) + (nota_10_caixa * 10) + (nota_5_caixa * 5) + (nota_2_caixa * 2) + (
                    moeda_1_caixa * 1) + (moeda_50_caixa * 0.50) + (moeda_25_caixa * 0.25) + (moeda_10_caixa * 0.10) + (
                                        moeda_5_caixa * 0.05)
        print(f'\nAqui segue o valor total do caixa: {valor_total_caixa}')
        continuar = int(input('\nDeseja continuar com o programa? SIM(1) ou NÃO(2): '))
        if continuar == 2:
            run_program = 0