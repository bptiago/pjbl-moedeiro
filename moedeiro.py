# Programa criado pelos alunos: João Vitor de Freitas e Tiago Bisolo Prestes - Turma BSI 2023/1

# Declaração de variáveis globais. Seu valor não é redefinido ao passar de um loop para outro
nota_20_caixa = 2
nota_10_caixa = 3
nota_5_caixa = 4
nota_2_caixa = 5
moeda_1_caixa = 5
moeda_50_caixa = 5
moeda_25_caixa = 5
moeda_10_caixa = 10
moeda_5_caixa = 10

estoque_lata_coca = 5
estoque_lata_redbull = 5
estoque_lata_agua = 5

vendas_coca = 0
vendas_redbull = 0
vendas_agua = 0

tentativas = 3
primeiro_uso = 1
rodar_programa = 1

valor_total_caixa = (nota_20_caixa * 20) + (nota_10_caixa * 10) + (nota_5_caixa * 5) + (nota_2_caixa * 2) + (
            moeda_1_caixa * 1) + (moeda_50_caixa * 0.50) + (moeda_25_caixa * 0.25) + (moeda_10_caixa * 0.10) + (
                                moeda_5_caixa * 0.05)

while rodar_programa == 1:

    print("Deseja acessar o modo consumidor ou admin?")
    modo = int(input("Para acessar o modo consumidor, digite 1, já para o modo Admin, digite 2: "))

    if modo != 1 and modo != 2:
        while modo != 1 and modo != 2:
            print("Insira um comando válido")
            modo = int(input("Para acessar o modo consumidor, digite 1, já para o modo Admin, digite 2: "))

    if modo == 1:
        if estoque_lata_agua == estoque_lata_coca == estoque_lata_redbull == 0 or valor_total_caixa == 0:
            if estoque_lata_agua == estoque_lata_coca == estoque_lata_redbull == 0:
                print("Sem produtos no estoque!")
                continuar = int(input("Deseja continuar com o programa? SIM(1) ou NÃO(2): "))
                while continuar != 1 and continuar != 2:
                    continuar = int(input("Deseja continuar com o programa? SIM(1) ou NÃO(2): "))
                if continuar == 2:
                    rodar_programa = 0
            else:
                print("Sem troco disponivel!")
                continuar = int(input("Deseja continuar com o programa? SIM(1) ou NÃO(2): "))
                while continuar != 1 and continuar != 2:
                    continuar = int(input("Deseja continuar com o programa? SIM(1) ou NÃO(2): "))
                if continuar == 2:
                    rodar_programa = 0

        else:
            print()
            print("MÁQUINA DE REFRIGERANTE")
            print("---------------------------------")
            print("(1) Coca-Cola 350ml - R$5,00")
            print("(2) RedBull 350ml - R$8,00")
            print("(3) Água sem gas 500ml - R$3,50")
            print("---------------------------------")

            bebida = int(input("\nEscolha sua bebida (1|2|3): "))

            while bebida != 1 and bebida != 2 and bebida != 3:
                print("\nValor inválido, favor escolher uma das 3 opções!")
                bebida = int(input("Escolha sua bebida (1|2|3): "))

            while bebida == 1 and estoque_lata_coca == 0:
                print("\nFavor escolher outra bebida, Coca-Cola fora de estoque")
                bebida = int(input("Escolha sua bebida (2|3): "))

            while bebida == 2 and estoque_lata_redbull == 0:
                print("\nFavor escolher outra bebida, RedBull fora de estoque")
                bebida = int(input("Escolha sua bebida (1|3): "))

            while bebida == 3 and estoque_lata_agua == 0:
                print("\nFavor escolher outra bebida, Água fora de estoque")
                bebida = int(input("Escolha sua bebida (1|2): "))

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

            while saldo_inserido < custo_bebida:
                print("\nFavor inserir saldo via moedas ou cédulas\nSaldo atual: ", saldo_inserido,
                      "reais\nCusto da bebida: ", custo_bebida, "reais")
                print(
                    "Para inserir: \n20 reais (1)\n10 reais (2)\n5 reais (3)\n2 reais (4)\n1 real (5)\n50 centavos (6)\n25 centavos (7)\n10 centavos (8)\n5 centavos (9)\nCancelar compra e devolver valor inserido (0)\n")
                valor_inserido = int(input("Insira o comando: "))
                print("---------------------------------")

                while valor_inserido < 0 or valor_inserido > 9:
                    print("\nValor inválido, favor escolher uma das 9 opções!")
                    print(
                        "Para inserir: \n20 reais (1)\n10 reais (2)\n5 reais (3)\n2 reais (4)\n1 real (5)\n50 centavos (6)\n25 centavos (7)\n10 centavos (8)\n5 centavos (9)\nCancelar compra e devolver valor inserido (0)\n")
                    valor_inserido = int(input("Insira o comando: "))
                    print("---------------------------------")

                if valor_inserido == 1:
                    saldo_inserido += 20
                    print("\nSaldo atual: ", saldo_inserido, "reais")
                    nota_20_inserida += 1

                elif valor_inserido == 2:
                    saldo_inserido += 10
                    print("\nSaldo atual: ", saldo_inserido, "reais")
                    nota_10_inserida += 1

                elif valor_inserido == 3:
                    saldo_inserido += 5
                    print("\nSaldo atual: ", saldo_inserido, "reais")
                    nota_5_inserida += 1

                elif valor_inserido == 4:
                    saldo_inserido += 2
                    print("\nSaldo atual: ", saldo_inserido, "reais")
                    nota_2_inserida += 1

                elif valor_inserido == 5:
                    saldo_inserido += 1
                    print("\nSaldo atual: ", saldo_inserido, "reais")
                    moeda_1_inserida += 1

                elif valor_inserido == 6:
                    saldo_inserido += 0.50
                    print("\nSaldo atual: ", saldo_inserido, "reais")
                    moeda_50_inserida += 1

                elif valor_inserido == 7:
                    saldo_inserido += 0.25
                    print(f"\nSaldo atual: ", saldo_inserido, "reais")
                    moeda_25_inserida += 1

                elif valor_inserido == 8:
                    saldo_inserido += 0.10
                    print("\nSaldo atual: ", saldo_inserido, "reais")
                    moeda_10_inserida += 1

                elif valor_inserido == 9:
                    saldo_inserido += 0.05
                    print("\nSaldo atual: ", saldo_inserido, "reais")
                    moeda_5_inserida += 1

                elif valor_inserido == 0:
                    if saldo_inserido != 0:
                        print("Devolvendo seu saldo de", saldo_inserido)
                    saldo_inserido = custo_bebida
                    print("Compra cancelada")

                if saldo_inserido > custo_bebida:
                    troco = saldo_inserido - custo_bebida
                    print("Seu troco será de", troco, "reais\n")
                else:
                    troco = 0

            if valor_inserido != 0:
                if troco == 0:
                    nota_20_caixa += nota_20_inserida
                    nota_10_caixa += nota_10_inserida
                    nota_5_caixa += nota_5_inserida
                    nota_2_caixa += nota_2_inserida
                    moeda_1_caixa += moeda_1_inserida
                    moeda_50_caixa += moeda_50_inserida
                    moeda_25_caixa += moeda_25_inserida
                    moeda_10_caixa += moeda_10_inserida
                    moeda_5_caixa += moeda_5_inserida

                    if bebida == 1:
                        estoque_lata_coca -= 1
                        vendas_coca += 1
                    elif bebida == 2:
                        estoque_lata_redbull -= 1
                        vendas_redbull += 1
                    elif bebida == 3:
                        estoque_lata_agua -= 1
                        vendas_agua += 1

                    print("Seu troco é de", troco, "reais")
                    print(
                        "\nLiberando o produto!\nObrigado por comprar com a gente!\n---------------------------------")

                while troco > 0:
                    contador_nota_20 = nota_20_inserida

                    contador_nota_10 = nota_10_inserida
                    contador_nota_10_caixa = nota_10_caixa

                    contador_nota_5 = nota_5_inserida
                    contador_nota_5_caixa = nota_5_caixa

                    contador_nota_2 = nota_2_inserida
                    contador_nota_2_caixa = nota_2_caixa

                    contador_moeda_1 = moeda_1_inserida
                    contador_moeda_1_caixa = moeda_1_caixa

                    contador_moeda_50 = moeda_50_inserida
                    contador_moeda_50_caixa = moeda_50_caixa

                    contador_moeda_25 = moeda_25_inserida
                    contador_moeda_25_caixa = moeda_25_caixa

                    contador_moeda_10 = moeda_10_inserida
                    contador_moeda_10_caixa = moeda_10_caixa

                    contador_moeda_5 = moeda_5_inserida
                    contador_moeda_5_caixa = moeda_5_caixa

                    contador_nota_10_troco = 0
                    contador_nota_5_troco = 0
                    contador_nota_2_troco = 0
                    contador_moeda_1_troco = 0
                    contador_moeda_50_troco = 0
                    contador_moeda_25_troco = 0
                    contador_moeda_10_troco = 0
                    contador_moeda_5_troco = 0

                    while troco >= 10 and nota_10_caixa > 0 or troco >= 10 and nota_10_inserida > 0:
                        if nota_10_inserida > 0:
                            troco = troco - 10
                            nota_10_inserida -= 1
                        else:
                            troco = troco - 10
                            nota_10_caixa -= 1
                            contador_nota_10_troco += 1

                    while troco >= 5 and nota_5_caixa > 0 or troco >= 5 and nota_5_inserida > 0:
                        if nota_5_inserida > 0:
                            troco = troco - 5
                            nota_5_inserida -= 1
                        else:
                            troco = troco - 5
                            nota_5_caixa -= 1
                            contador_nota_5_troco += 1

                    while troco >= 2 and nota_2_caixa > 0 or troco >= 2 and nota_2_inserida > 0:
                        if nota_2_inserida > 0:
                            troco = troco - 2
                            nota_2_inserida -= 1
                        else:
                            troco = troco - 2
                            nota_2_caixa -= 1
                            contador_nota_2_troco += 1

                    while troco >= 1 and moeda_1_caixa > 0 or troco >= 1 and moeda_1_inserida > 0:
                        if moeda_1_inserida > 0:
                            troco = troco - 1
                            moeda_1_inserida -= 1
                        else:
                            troco = troco - 1
                            moeda_1_caixa -= 1
                            contador_moeda_1_troco += 1

                    while troco >= 0.50 and moeda_50_caixa > 0 or troco >= 0.50 and moeda_50_inserida > 0:
                        if moeda_50_inserida > 0:
                            troco = troco - 0.50
                            moeda_50_inserida -= 1
                        else:
                            troco = troco - 0.50
                            moeda_50_caixa -= 1
                            contador_moeda_50_troco += 1

                    while troco >= 0.25 and moeda_25_caixa > 0 or troco >= 0.25 and moeda_25_inserida > 0:
                        if moeda_25_inserida > 0:
                            troco = troco - 0.25
                            moeda_25_inserida -= 1
                        else:
                            troco = troco - 0.25
                            moeda_25_caixa -= 1
                            contador_moeda_25_troco += 1

                    while troco >= 0.10 and moeda_10_caixa > 0 or troco >= 0.10 and moeda_10_inserida > 0:
                        if moeda_10_inserida > 0:
                            troco = troco - 0.10
                            moeda_10_inserida -= 1
                        else:
                            troco = troco - 0.10
                            moeda_10_caixa -= 1
                            contador_moeda_10_troco += 1

                    while troco >= 0.05 and moeda_5_caixa > 0 or troco >= 0.05 and moeda_5_inserida > 0:
                        if moeda_5_inserida > 0:
                            troco = troco - 0.05
                            moeda_5_inserida -= 1
                        else:
                            troco = troco - 0.05
                            moeda_5_caixa -= 1
                            contador_moeda_5_troco += 1

                    if troco > 0:
                        troco = 0

                        print("Devolvendo", contador_nota_20, "nota(s) de 20 reais\nDevolvendo", contador_nota_10,
                              "nota(s) de 10 reais\nDevolvendo", contador_nota_5, "nota(s) de 5 reais\nDevolvendo",
                              contador_nota_2, "nota(s) de 2 reais\nDevolvendo", contador_moeda_1,
                              "moeda(s) de 1 real\nDevolvendo", contador_moeda_50, "nota(s) de 50 centavos\nDevolvendo",
                              contador_moeda_25, "nota(s) de 25 centavos\nDevolvendo", contador_moeda_10,
                              "nota(s) de 10 centavos\nDevolvendo", contador_moeda_5, "nota(s) de 5 centavos")

                        nota_10_caixa = contador_nota_10_caixa
                        nota_5_caixa = contador_nota_5_caixa
                        nota_2_caixa = contador_nota_2_caixa
                        moeda_1_caixa = contador_moeda_1_caixa
                        moeda_50_caixa = contador_moeda_50_caixa
                        moeda_25_caixa = contador_moeda_25_caixa
                        moeda_10_caixa = contador_moeda_10_caixa
                        moeda_5_caixa = contador_moeda_5_caixa

                    else:
                        contador_nota_10_troco = contador_nota_10_troco + (contador_nota_10 - nota_10_inserida)
                        contador_nota_5_troco = contador_nota_5_troco + (contador_nota_5 - nota_5_inserida)
                        contador_nota_2_troco = contador_nota_2_troco + (contador_nota_2 - nota_2_inserida)
                        contador_moeda_1_troco = contador_moeda_1_troco + (contador_moeda_1 - moeda_1_inserida)
                        contador_moeda_50_troco = contador_moeda_50_troco + (contador_moeda_50 - moeda_50_inserida)
                        contador_moeda_25_troco = contador_moeda_25_troco + (contador_moeda_25 - moeda_25_inserida)
                        contador_moeda_10_troco = contador_moeda_10_troco + (contador_moeda_10 - moeda_10_inserida)
                        contador_moeda_5_troco = contador_moeda_5_troco + (contador_moeda_5 - moeda_5_inserida)

                        print("Devolvendo", contador_nota_10_troco, "nota(s) de 10 reais\nDevolvendo",
                              contador_nota_5_troco, "nota(s) de 5 reais\nDevolvendo", contador_nota_2_troco,
                              "nota(s) de 2 reais\nDevolvendo", contador_moeda_1_troco,
                              "moeda(s) de 1 real\nDevolvendo", contador_moeda_50_troco,
                              "nota(s) de 50 centavos\nDevolvendo", contador_moeda_10_troco,
                              "nota(s) de 10 centavos\nDevolvendo", contador_moeda_5_troco, "nota(s) de 5 centavos")

                        nota_20_caixa += nota_20_inserida
                        nota_10_caixa += nota_10_inserida
                        nota_5_caixa += nota_5_inserida
                        nota_2_caixa += nota_2_inserida
                        moeda_1_caixa += moeda_1_inserida
                        moeda_50_caixa += moeda_50_inserida
                        moeda_25_caixa += moeda_25_inserida
                        moeda_10_caixa += moeda_10_inserida
                        moeda_5_caixa += moeda_5_inserida

                        if bebida == 1:
                            estoque_lata_coca -= 1
                            vendas_coca += 1
                        elif bebida == 2:
                            estoque_lata_redbull -= 1
                            vendas_redbull += 1
                        elif bebida == 3:
                            estoque_lata_agua -= 1
                            vendas_agua += 1

                        print(
                            "\nLiberando o produto\nObrigado por comprar com a gente!\n---------------------------------")

            continuar = int(input("Deseja continuar com o programa? SIM(1) ou NÃO(2): "))
            while continuar != 1 and continuar != 2:
                continuar = int(input("Deseja continuar com o programa? SIM(1) ou NÃO(2): "))

            if continuar == 2:
                rodar_programa = 0
    else:
        print("\n--------------------------------- \nSeja Bem-vindo ao modo Admin\n")

        if primeiro_uso == 1:
            senha_escolhida = int(input("Escolha uma senha com somente números inteiros: "))
            senha_confirma = int(input("Confirme sua senha: "))
            while senha_escolhida != senha_confirma:
                print("Senhas diferentes")
                senha_escolhida = int(input("Escolha uma senha com somente números inteiros: "))
                senha_confirma = int(input("Confirme sua senha: "))
            primeiro_uso -= 1
            senha = senha_confirma

        else:
            senha = int(input("Favor inserir senha escolhida: "))

        if senha != senha_escolhida:
            while tentativas > 0 and senha != senha_escolhida:
                print("Senha incorreta\nTentativas restantes: ", tentativas)
                senha = int(input("Favor inserir senha escolhida: "))
                tentativas -= 1

        else:
            valor_total_caixa = (nota_20_caixa * 20) + (nota_10_caixa * 10) + (nota_5_caixa * 5) + (
                    nota_2_caixa * 2) + (moeda_1_caixa * 1) + (moeda_50_caixa * 0.50) + (moeda_25_caixa * 0.25) + (
                                        moeda_10_caixa * 0.10) + (moeda_5_caixa * 0.05)

            print("\nAqui segue o número de moedas e cédulas de cada tipo:\nCédulas de 20 reais: ", nota_20_caixa,
                  "\nCédulas de 10 reais: ", nota_10_caixa, "\nCédulas de 5 reais: ", nota_5_caixa,
                  "\nCédulas de 2 reais: ", nota_2_caixa, "\nMoedas de 1 real: ", moeda_1_caixa,
                  "\nMoedas de 50 centavos: ", moeda_50_caixa, "\nMoedas de 25 centavos: ", moeda_25_caixa,
                  "\nMoedas de 10 centavos: ", moeda_10_caixa, "\nMoedas de 5 centavos: ", moeda_5_caixa)

            opcao_saque_adicionar = int(input(
                "\nDeseja efetuar algum saque ou adicionar dinheiro ao caixa? Saque(1), Depositar dinheiro(2) e Seguir em frente(3): "))
            while opcao_saque_adicionar != 1 and opcao_saque_adicionar != 2 and opcao_saque_adicionar != 3:
                print("\nValor inválido, tente novamente")
                opcao_saque_adicionar = int(input(
                    "Deseja efetuar algum saque ou adicionar dinheiro ao caixa? Saque(1), Depositar dinheiro(2) e Seguir em frente(3): "))

            if opcao_saque_adicionar == 1:
                opcao_saque = int(input(
                    "Deseja sacar o valor total ou sacar diferentes notas/moedas? Valor total(1) Valor individual(2): "))
                while opcao_saque != 1 and opcao_saque != 2:
                    print("\nValor inválido, tente novamente")
                    print("Deseja sacar o valor total?", valor_total_caixa, "reais ou sacar diferentes notas/moedas?")
                    opcao_saque = int(input("Valor total(1) Valor individual(2): "))

                if opcao_saque == 1 and valor_total_caixa > 0:
                    print("Sacando o total de", valor_total_caixa, "reais")
                    nota_20_caixa = 0
                    nota_10_caixa = 0
                    nota_5_caixa = 0
                    nota_2_caixa = 0
                    moeda_1_caixa = 0
                    moeda_50_caixa = 0
                    moeda_25_caixa = 0
                    moeda_10_caixa = 0
                    moeda_5_caixa = 0

                elif opcao_saque == 2 and valor_total_caixa > 0:
                    valor_saque = int(input(
                        "\nPara sacar: \n20 reais (1)\n10 reais (2)\n5 reais (3)\n2 reais (4)\n1 real (5)\n50 centavos (6)\n25 centavos (7)\n10 centavos (8)\n5 centavos (9)\nTerminar Saque (0): "))

                    while valor_saque != 0:
                        if valor_saque == 1:
                            print(nota_20_caixa, "Nota(s) de 20 reais")
                            numero_saque = int(input("Deseja sacar quantas notas?\n"))
                            while numero_saque <= 0:
                                numero_saque = int(input("Digite um valor positivo:\n"))
                            if numero_saque <= nota_20_caixa:
                                nota_20_caixa -= numero_saque
                                print(numero_saque, "Nota(s) de 20 reais sacada\nNúmero de notas de 20 reais: ",
                                      nota_20_caixa)
                            else:
                                print("\nQuantidade inválida, favor tentar novamente\n")

                        elif valor_saque == 2:
                            print(nota_10_caixa, "Nota(s) de 10 reais")
                            numero_saque = int(input("Deseja sacar quantas notas?\n"))
                            while numero_saque <= 0:
                                numero_saque = int(input("Digite um valor positivo:\n"))
                            if numero_saque <= nota_10_caixa:
                                nota_10_caixa -= numero_saque
                                print(numero_saque, "Nota(s) de 10 reais sacada\nNúmero de notas de 10 reais: ",
                                      nota_10_caixa)
                            else:
                                print("\nQuantidade inválida, favor tentar novamente\n")

                        elif valor_saque == 3:
                            print(nota_5_caixa, "Nota(s) de 5 reais")
                            numero_saque = int(input("Deseja sacar quantas notas?\n"))
                            while numero_saque <= 0:
                                numero_saque = int(input("Digite um valor positivo:\n"))
                            if numero_saque <= nota_5_caixa:
                                nota_5_caixa -= numero_saque
                                print(numero_saque, "Nota(s) de 5 reais sacada\nNúmero de notas de 5 reais: ",
                                      nota_5_caixa)
                            else:
                                print("\nQuantidade inválida, favor tentar novamente\n")

                        elif valor_saque == 4:
                            print(nota_2_caixa, "Nota(s) de 2 reais")
                            numero_saque = int(input("Deseja sacar quantas notas?\n"))
                            while numero_saque <= 0:
                                numero_saque = int(input("Digite um valor positivo:\n"))
                            if numero_saque <= nota_2_caixa:
                                nota_2_caixa -= numero_saque
                                print(numero_saque, "Nota(s) de 2 reais sacada\nNúmero de notas de 20 reais: ",
                                      nota_2_caixa)
                            else:
                                print("\nQuantidade inválida, favor tentar novamente\n")

                        elif valor_saque == 5:
                            print(moeda_1_caixa, "Moeda(s) de 1 real")
                            numero_saque = int(input("Deseja sacar quantas moedas?\n"))
                            while numero_saque <= 0:
                                numero_saque = int(input("Digite um valor positivo:\n"))
                            if numero_saque <= moeda_1_caixa:
                                moeda_1_caixa -= numero_saque
                                print(numero_saque, "Moeda(s) de 1 real sacada\nNúmero de moedas de 1 real: ",
                                      moeda_1_caixa)
                            else:
                                print("\nQuantidade inválida, favor tentar novamente\n")

                        elif valor_saque == 6:
                            print(moeda_50_caixa, "Moeda(s) de 50 centavos")
                            numero_saque = int(input("Deseja sacar quantas moedas?\n"))
                            while numero_saque <= 0:
                                numero_saque = int(input("Digite um valor positivo:\n"))
                            if numero_saque <= moeda_50_caixa:
                                moeda_50_caixa -= numero_saque
                                print(numero_saque, "Moeda(s) de 50 centavos sacada\nNúmero de moedas de 50 centavos: ",
                                      moeda_50_caixa)
                            else:
                                print("\nQuantidade inválida, favor tentar novamente\n")

                        elif valor_saque == 7:
                            print(moeda_25_caixa, "Moeda(s) de 25 centavos")
                            numero_saque = int(input("Deseja sacar quantas moedas?\n"))
                            while numero_saque <= 0:
                                numero_saque = int(input("Digite um valor positivo:\n"))
                            if numero_saque <= moeda_25_caixa:
                                moeda_25_caixa -= numero_saque
                                print(numero_saque, "Moeda(s) de 25 centavos sacada\nNúmero de moedas de 25 centavos: ",
                                      moeda_25_caixa)
                            else:
                                print("\nQuantidade inválida, favor tentar novamente\n")

                        elif valor_saque == 8:
                            print(moeda_10_caixa, "Moeda(s) de 10 centavos")
                            numero_saque = int(input("Deseja sacar quantas moedas?\n"))
                            while numero_saque <= 0:
                                numero_saque = int(input("Digite um valor positivo:\n"))
                            if numero_saque <= moeda_10_caixa:
                                moeda_10_caixa -= numero_saque
                                print(numero_saque, "Moeda(s) de 10 centavos sacada\nNúmero de moedas de 10 centavos: ",
                                      moeda_10_caixa)
                            else:
                                print("\nQuantidade inválida, favor tentar novamente\n")

                        elif valor_saque == 9:
                            print(moeda_5_caixa, "Moeda(s) de 5 centavos")
                            numero_saque = int(input("Deseja sacar quantas moedas?\n"))
                            while numero_saque <= 0:
                                numero_saque = int(input("Digite um valor positivo:\n"))
                            if numero_saque <= moeda_5_caixa:
                                moeda_5_caixa -= numero_saque
                                print(numero_saque, "Moeda(s) de 5 centavos sacada\nNúmero de moedas de 5 centavos: ",
                                      moeda_5_caixa)
                            else:
                                print("\nQuantidade inválida, favor tentar novamente\n")

                        else:
                            print("\nValor Inválido")

                        valor_saque = int(input(
                            "\nPara sacar: \n20 reais (1)\n10 reais (2)\n5 reais (3)\n2 reais (4)\n1 real (5)\n50 centavos (6)\n25 centavos (7)\n10 centavos (8)\n5 centavos (9)\nTerminar Saque (0): "))
                        print()

            elif opcao_saque_adicionar == 2:
                valor_deposito = int(input(
                    "\nPara depositar: \n20 reais (1)\n10 reais (2)\n5 reais (3)\n2 reais (4)\n1 real (5)\n50 centavos (6)\n25 centavos (7)\n10 centavos (8)\n5 centavos (9)\nTerminar Deposito (0): "))
                while valor_deposito != 0:
                    if valor_deposito == 1:
                        print(nota_20_caixa, "Nota(s) dentro do caixa")
                        numero_deposito = int(input("Deseja depositar quantas notas?\n"))
                        while numero_deposito <= 0:
                            numero_deposito = int(input("Digite um valor positivo:\n"))
                        nota_20_caixa += numero_deposito
                        print(numero_deposito, "Nota(s) de 20 reais depositadas\nNúmero de notas de 20 reais: ",
                              nota_20_caixa)

                    elif valor_deposito == 2:
                        print(nota_10_caixa, "Nota(s) dentro do caixa")
                        numero_deposito = int(input("Deseja depositar quantas notas?\n"))
                        while numero_deposito <= 0:
                            numero_deposito = int(input("Digite um valor positivo:\n"))
                        nota_10_caixa += numero_deposito
                        print(numero_deposito, "Nota(s) de 10 reais depositadas\nNúmero de notas de 10 reais: ",
                              nota_10_caixa)

                    elif valor_deposito == 3:
                        print(nota_5_caixa, "Nota(s) dentro do caixa")
                        numero_deposito = int(input("Deseja depositar quantas notas?\n"))
                        while numero_deposito <= 0:
                            numero_deposito = int(input("Digite um valor positivo:\n"))
                        nota_5_caixa += numero_deposito
                        print(numero_deposito, "Nota(s) de 5 reais depositadas\nNúmero de notas de 5 reais: ",
                              nota_5_caixa)

                    elif valor_deposito == 4:
                        print(nota_2_caixa, "Nota(s) dentro do caixa")
                        numero_deposito = int(input("Deseja depositar quantas notas?\n"))
                        while numero_deposito <= 0:
                            numero_deposito = int(input("Digite um valor positivo:\n"))
                        nota_2_caixa += numero_deposito
                        print(numero_deposito, "Nota(s) de 2 reais depositadas\nNúmero de notas de 2 reais: ",
                              nota_2_caixa)

                    elif valor_deposito == 5:
                        print(moeda_1_caixa, "Moeda(s) dentro do caixa")
                        numero_deposito = int(input("Deseja depositar quantas moedas?\n"))
                        while numero_deposito <= 0:
                            numero_deposito = int(input("Digite um valor positivo:\n"))
                        moeda_1_caixa += numero_deposito
                        print(numero_deposito, "Moeda(s) de 1 real depositadas\nNúmero de moedas de 1 real: ",
                              moeda_1_caixa)

                    elif valor_deposito == 6:
                        print(moeda_50_caixa, "Moeda(s) dentro do caixa")
                        numero_deposito = int(input("Deseja depositar quantas moedas?\n"))
                        while numero_deposito <= 0:
                            numero_deposito = int(input("Digite um valor positivo:\n"))
                        moeda_50_caixa += numero_deposito
                        print(numero_deposito, "Moeda(s) de 50 centavos depositadas\nNúmero de moedas de 50 centavos: ",
                              moeda_50_caixa)

                    elif valor_deposito == 7:
                        print(moeda_25_caixa, "Moeda(s) dentro do caixa")
                        numero_deposito = int(input("Deseja depositar quantas moedas?\n"))
                        while numero_deposito <= 0:
                            numero_deposito = int(input("Digite um valor positivo:\n"))
                        moeda_25_caixa += numero_deposito
                        print(numero_deposito, "Moeda(s) de 25 centavos depositadas\nNúmero de moedas de 25 centavos: ",
                              moeda_25_caixa)

                    elif valor_deposito == 8:
                        print(moeda_10_caixa, "Moeda(s) dentro do caixa")
                        numero_deposito = int(input("Deseja depositar quantas moedas?\n"))
                        while numero_deposito <= 0:
                            numero_deposito = int(input("Digite um valor positivo:\n"))
                        moeda_10_caixa += numero_deposito
                        print(numero_deposito, "Moeda(s) de 10 centavos depositadas\nNúmero de moedas de 10 centavos: ",
                              moeda_10_caixa)

                    elif valor_deposito == 9:
                        print(moeda_5_caixa, "Moeda(s) dentro do caixa")
                        numero_deposito = int(input("Deseja depositar quantas moedas?\n"))
                        while numero_deposito <= 0:
                            numero_deposito = int(input("Digite um valor positivo:\n"))
                        moeda_5_caixa += numero_deposito
                        print(numero_deposito, "Moeda(s) de 5 centavos depositadas\nNúmero de moedas de 5 centavos: ",
                              moeda_5_caixa)

                    else:
                        print("\nValor Invalido")

                    valor_deposito = int(input(
                        "\nPara depositar: \n20 reais (1)\n10 reais (2)\n5 reais (3)\n2 reais (4)\n1 real (5)\n50 centavos (6)\n25 centavos (7)\n10 centavos (8)\n5 centavos (9)\nTerminar Deposito (0):\n"))

            faturamento_coca = vendas_coca * 5
            faturamento_redbull = vendas_redbull * 8
            faturamento_agua = vendas_agua * 3.50

            print("\nAqui seguem o numero de vendas e seu faturamento:\nForam vendidas", vendas_coca,
                  "latas de Coca-Cola e um total de faturamento de", faturamento_coca,
                  "reais\nForam vendidas", vendas_redbull, "latas de Redbull e um total de faturamento de",
                  faturamento_redbull,
                  "reais\nForam vendidas", vendas_agua, "latas de Água e um total de faturamento de", faturamento_agua,
                  "reais")

            print("\nAqui segue o número de latas em seu estoque:\nCoca-Cola: ", estoque_lata_coca, "\nRedBull: ",
                  estoque_lata_redbull, "\nAgua: ", estoque_lata_agua)

            adicionar_latas = int(input("Deseja adicionar mais latas? Sim(1) ou Não(2): "))

            while adicionar_latas != 1 and adicionar_latas != 2:
                print("\nValor inválido, tente novamente")
                adicionar_latas = int(input("Deseja adicionar mais latas? Sim(1) ou Não(2): "))

            if adicionar_latas == 1:
                adicionar_latas_escolher = int(input(
                    "\n(1) Coca-Cola 350ml\n(2) RedBull 350ml\n(3) Água sem gas 500ml\nEscolha a bebida a estocar: "))

                while adicionar_latas_escolher != 1 and adicionar_latas_escolher != 2 and adicionar_latas_escolher != 3:
                    print("\nValor inválido, favor escolher uma das 3 opções!")
                    adicionar_latas_escolher = int(input("Escolha sua bebida (1|2|3)"))

                if adicionar_latas_escolher == 1:
                    adicionar_coca = int(input("Quantas latas de Coca-Cola você deseja adicionar? "))
                    while adicionar_coca <= 0:
                        print("Digite um número válido")
                        adicionar_coca = int(input("Quantas latas de Coca-Cola você deseja adicionar? "))

                    estoque_lata_coca += adicionar_coca
                    print("Novo estoque: ", estoque_lata_coca, "latas")

                if adicionar_latas_escolher == 2:
                    adicionar_RedBull = int(input("Quantas latas de RedBull você deseja adicionar? "))
                    while adicionar_RedBull <= 0:
                        print("Digite um número válido")
                        adicionar_RedBull = int(input("Quantas latas de RedBull você deseja adicionar? "))

                    estoque_lata_redbull += adicionar_RedBull
                    print("Novo estoque: ", estoque_lata_redbull, "latas")

                if adicionar_latas_escolher == 3:
                    adicionar_agua = int(input("Quantas latas de Água você deseja adicionar? "))
                    while adicionar_agua <= 0:
                        print("Digite um número válido")
                        adicionar_agua = int(input("Quantas latas de Água você deseja adicionar? "))

                    estoque_lata_agua += adicionar_agua
                    print("Novo estoque: ", estoque_lata_agua, "latas")

            valor_total_caixa = (nota_20_caixa * 20) + (nota_10_caixa * 10) + (nota_5_caixa * 5) + (
                    nota_2_caixa * 2) + (moeda_1_caixa * 1) + (moeda_50_caixa * 0.50) + (moeda_25_caixa * 0.25) + (
                                        moeda_10_caixa * 0.10) + (moeda_5_caixa * 0.05)
            print("\nAqui segue o valor total do caixa: ", valor_total_caixa)

            if valor_total_caixa == 0:
                adicionar_caixa_emergencia = int(input(
                    "\nFavor adicionar dinheiro ao caixa, caso contrário, a máquina deixara de realizar vendas\nAdicionar agora(1) ou Adicionar depois(2): "))

                if adicionar_caixa_emergencia == 1:
                    valor_deposito = int(input(
                        "Para depositar: \n20 reais (1)\n10 reais (2)\n5 reais (3)\n2 reais (4)\n1 real (5)\n50 centavos (6)\n25 centavos (7)\n10 centavos (8)\n5 centavos (9)\nTerminar Deposito (0): "))

                    while valor_deposito != 0:
                        if valor_deposito == 1:
                            print(nota_20_caixa, "Nota(s)")
                            numero_deposito = int(input("Deseja depositar quantas notas?\n"))
                            while numero_deposito <= 0:
                                numero_deposito = int(input("Digite um valor positivo:\n"))
                            nota_20_caixa += numero_deposito
                            print(numero_deposito, "Nota(s) de 20 reais depositadas\nNúmero de notas de 20 reais: ",
                                  nota_20_caixa)

                        elif valor_deposito == 2:
                            print(nota_10_caixa, "Nota(s)")
                            numero_deposito = int(input("Deseja depositar quantas notas?\n"))
                            while numero_deposito <= 0:
                                numero_deposito = int(input("Digite um valor positivo:\n"))
                            nota_10_caixa += numero_deposito
                            print(numero_deposito, "Nota(s) de 10 reais depositadas\nNúmero de notas de 10 reais: ",
                                  nota_10_caixa)

                        elif valor_deposito == 3:
                            print(nota_5_caixa, "Nota(s)")
                            numero_deposito = int(input("Deseja depositar quantas notas?\n"))
                            while numero_deposito <= 0:
                                numero_deposito = int(input("Digite um valor positivo:\n"))
                            nota_5_caixa += numero_deposito
                            print(numero_deposito, "Nota(s) de 5 reais depositadas\nNúmero de notas de 5 reais: ",
                                  nota_5_caixa)

                        elif valor_deposito == 4:
                            print(nota_2_caixa, "Nota(s)")
                            numero_deposito = int(input("Deseja depositar quantas notas?\n"))
                            while numero_deposito <= 0:
                                numero_deposito = int(input("Digite um valor positivo:\n"))
                            nota_2_caixa += numero_deposito
                            print(numero_deposito, "Nota(s) de 2 reais depositadas\nNúmero de notas de 2 reais: ",
                                  nota_2_caixa)

                        elif valor_deposito == 5:
                            print(moeda_1_caixa, "Moeda(s)")
                            numero_deposito = int(input("Deseja depositar quantas moedas?\n"))
                            while numero_deposito <= 0:
                                numero_deposito = int(input("Digite um valor positivo:\n"))
                            moeda_1_caixa += numero_deposito
                            print(numero_deposito, "Moeda(s) de 1 real depositadas\nNúmero de moedas de 1 real: ",
                                  moeda_1_caixa)

                        elif valor_deposito == 6:
                            print(moeda_50_caixa, "Moeda(s)")
                            numero_deposito = int(input("Deseja depositar quantas moedas?\n"))
                            while numero_deposito <= 0:
                                numero_deposito = int(input("Digite um valor positivo:\n"))
                            moeda_50_caixa += numero_deposito
                            print(numero_deposito,
                                  "Moeda(s) de 50 centavos depositadas\nNúmero de moedas de 50 centavos: ",
                                  moeda_50_caixa)

                        elif valor_deposito == 7:
                            print(moeda_25_caixa, "Moeda(s)")
                            numero_deposito = int(input("Deseja depositar quantas moedas?\n"))
                            while numero_deposito <= 0:
                                numero_deposito = int(input("Digite um valor positivo:\n"))
                            moeda_25_caixa += numero_deposito
                            print(numero_deposito,
                                  "Moeda(s) de 25 centavos depositadas\nNúmero de moedas de 25 centavos: ",
                                  moeda_25_caixa)

                        elif valor_deposito == 8:
                            print(moeda_10_caixa, "Moeda(s)")
                            numero_deposito = int(input("Deseja depositar quantas moedas?\n"))
                            while numero_deposito <= 0:
                                numero_deposito = int(input("Digite um valor positivo:\n"))
                            moeda_10_caixa += numero_deposito
                            print(numero_deposito,
                                  "Moeda(s) de 10 centavos depositadas\nNúmero de moedas de 10 centavos: ",
                                  moeda_10_caixa)

                        elif valor_deposito == 9:
                            print(moeda_5_caixa, "Moeda(s)")
                            numero_deposito = int(input("Deseja depositar quantas moedas?\n"))
                            while numero_deposito <= 0:
                                numero_deposito = int(input("Digite um valor positivo:\n"))
                            moeda_5_caixa += numero_deposito
                            print(numero_deposito,
                                  "Moeda(s) de 5 centavos depositadas\nNúmero de moedas de 5 centavos: ", moeda_5_caixa)

                        else:
                            print("\nValor Inválido")

                        valor_deposito = int(input(
                            "Para depositar: \n20 reais (1)\n10 reais (2)\n5 reais (3)\n2 reais (4)\n1 real (5)\n50 centavos (6)\n25 centavos (7)\n10 centavos (8)\n5 centavos (9)\nTerminar Deposito (0): "))

        continuar = int(input("Deseja continuar com o programa? SIM(1) ou NÃO(2): "))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Deseja continuar com o programa? SIM(1) ou NÃO(2): "))

        if continuar == 2:
            rodar_programa = 0
