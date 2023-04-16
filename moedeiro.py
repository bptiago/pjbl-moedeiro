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
estoque_lata_redbull = 5
estoque_lata_agua = 5
tentativas = 3
primeiro_uso = 1

while run_program == 1:

    print("Deseja acessar o modo de consumidor ou admin?")
    modo = int(input("Para acessar o modo consumidor, digite 1, já para o modo Admin, digite 2: "))
    if modo != 1 and modo != 2:
        while modo != 1 and modo != 2:
            print("Insira um comando válido")
            modo = int(input("Para acessar o modo consumidor, digite 1, ja para o modo Admin, digite 2: "))
    if modo == 1:
        if estoque_lata_agua == estoque_lata_coca == estoque_lata_redbull == 0:
            print("Sem produtos no estoque!")
            continuar = int(input("Deseja continuar com o programa? SIM(1) ou NÃO(2): "))
            while continuar != 1 and continuar != 2:
                continuar = int(input("Deseja continuar com o programa? SIM(1) ou NÃO(2): "))

            if continuar == 2:
                run_program = 0

        else:
            print(
                "\nMÁQUINA DE REFRIGERANTE \n--------------------------------- \n(1) Coca-Cola 350ml - R$5,00 \n(2) RedBull 350ml - R$8,00 \n(3) Água sem gas 500ml - R$3,50 \n---------------------------------")

            bebida = int(input("\nEscolha sua bebida (1|2|3): "))
            while bebida != 1 and bebida != 2 and bebida != 3:
                print("\nValor inválido, favor escolher uma das 3 opções!")
                bebida = int(input("Escolha sua bebida (1|2|3): "))

            while bebida == 1 and estoque_lata_coca == 0:
                print("\nFavor escolher outra bebida, Coca-Cola fora de estoque")
                bebida = int(input("Escolha sua bebida (2|3): "))

            while bebida == 2 and estoque_lata_redbull == 0:
                print("\nFavor escolher outra bebida, Redbull fora de estoque")
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
                print("Para inserir: \n20 reais (1)\n10 reais (2)\n5 reais (3)\n2 reais (4)\n1 real (5)\n50 centavos (6)\n25 centavos (7)\n10 centavos (8)\n5 centavos (9)\nCancelar compra e devolver valor inserido (0)\n")
                valor_inserido = int(input("Insira o comando: "))
                print("---------------------------------")
                while valor_inserido < 0 or valor_inserido > 9:
                    print("\nValor invalido, favor escolher uma das 9 opções!")
                    print(
                        "Para inserir: \n20 reais (1)\n10 reais (2)\n5 reais (3)\n2 reais (4)\n1 real (5)\n50 centavos (6)\n25 centavos (7)\n10 centavos (8)\n5 centavos (9)\nCancelar compra e devolver valor inserido (0)\n")
                    valor_inserido = int(input("Insira o comando: "))
                    print("---------------------------------")

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

                elif valor_inserido == 0:
                    saldo_inserido = custo_bebida
                    print(f"Compra cancelada")

                if saldo_inserido >= custo_bebida:
                    troco = saldo_inserido - custo_bebida
                    print(f"Seu troco sera de {troco} reais\n")

            if valor_inserido != 0:
                # Seção nova. Caso o troco seja = 0:
                if troco == 0:
                    if nota_20_inserida > 0:
                        nota_20_caixa += nota_20_inserida

                    if nota_10_inserida > 0:
                        nota_10_caixa += nota_10_inserida

                    if nota_5_inserida > 0:
                        nota_5_caixa += nota_5_inserida

                    if nota_2_inserida > 0:
                        nota_2_caixa += nota_2_inserida

                    if moeda_1_inserida > 0:
                        moeda_1_caixa += moeda_1_inserida

                    if moeda_50_inserida > 0:
                        moeda_50_caixa += moeda_50_inserida

                    if moeda_25_inserida > 0:
                        moeda_25_caixa += moeda_25_inserida

                    if moeda_10_inserida > 0:
                        moeda_10_caixa += moeda_10_inserida

                    if moeda_5_inserida > 0:
                        moeda_5_caixa += moeda_5_inserida

                    if bebida == 1:
                        estoque_lata_coca -= 1
                    elif bebida == 2:
                        estoque_lata_redbull -= 1
                    elif bebida == 1:
                        estoque_lata_agua -= 1

                    print("\nLiberando o produto!")
                    print("Obrigado por comprar com a gente!\n")
                    print("---------------------------------")

                while troco > 0:
                    while troco >= 10 and nota_10_caixa > 0 or troco >= 10 and nota_10_inserida > 0:
                        if nota_10_inserida > 0:
                            troco = troco - 10
                            nota_10_inserida -= 1
                            contador_nota_10 += 1
                            print("Devolvendo uma nota de 10 reais")
                        else:
                            troco = troco - 10
                            nota_10_caixa -= 1
                            contador_nota_10 += 1
                            print("Devolvendo uma nota de 10 reais")

                    while troco >= 5 and nota_5_caixa > 0 or troco >= 5 and nota_5_inserida > 0:
                        if nota_5_inserida > 0:
                            troco = troco - 5
                            nota_5_inserida -= 1
                            contador_nota_5 += 1
                            print("Devolvendo uma nota de 5 reais")
                        else:
                            troco = troco - 5
                            nota_5_caixa -= 1
                            contador_nota_5 += 1
                            print("Devolvendo uma nota de 5 reais")

                    while troco >= 2 and nota_2_caixa > 0 or troco >= 2 and nota_2_inserida > 0:
                        if nota_2_inserida > 0:
                            troco = troco - 2
                            nota_2_inserida -= 1
                            contador_nota_2 += 1
                            print("Devolvendo uma nota de 2 reais")
                        else:
                            troco = troco - 2
                            nota_2_caixa -= 1
                            contador_nota_2 += 1
                            print("Devolvendo uma nota de 2 reais")

                    while troco >= 1 and moeda_1_caixa > 0 or troco >= 1 and moeda_1_inserida > 0:
                        if moeda_1_inserida > 0:
                            troco = troco - 1
                            moeda_1_inserida -= 1
                            contador_moeda_1 += 1
                            print("Devolvendo uma moeda de 1 real")
                        else:
                            troco = troco - 1
                            moeda_1_caixa -= 1
                            contador_moeda_1 += 1
                            print("Devolvendo uma moeda de 1 real")

                    while troco >= 0.50 and moeda_50_caixa > 0 or troco >= 0.50 and moeda_50_inserida > 0:
                        if moeda_50_inserida > 0:
                            troco = troco - 0.50
                            moeda_50_inserida -= 1
                            contador_moeda_50 += 1
                            print("Devolvendo uma moeda de 50 centavos")
                        else:
                            troco = troco - 0.50
                            moeda_50_caixa -= 1
                            contador_moeda_50 += 1
                            print("Devolvendo uma moeda de 50 centavos")

                    while troco >= 0.25 and moeda_25_caixa > 0 or troco >= 0.25 and moeda_25_inserida > 0:
                        if moeda_25_inserida > 0:
                            troco = troco - 0.25
                            moeda_25_inserida -= 1
                            contador_moeda_25 += 1
                            print("Devolvendo uma moeda de 25 centavos")
                        else:
                            troco = troco - 0.25
                            moeda_25_caixa -= 1
                            contador_moeda_25 += 1
                            print("Devolvendo uma moeda de 25 centavos")

                    while troco >= 0.10 and moeda_10_caixa > 0 or troco >= 0.10 and moeda_10_inserida > 0:
                        if moeda_10_inserida > 0:
                            troco = troco - 0.10
                            moeda_10_inserida -= 1
                            contador_moeda_10 += 1
                            print("Devolvendo uma moeda de 10 centavos")
                        else:
                            troco = troco - 0.10
                            moeda_10_caixa -= 1
                            contador_moeda_10 += 1
                            print("Devolvendo uma moeda de 10 centavos")

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
                    elif bebida == 2:
                        estoque_lata_redbull -= 1
                    elif bebida == 1:
                        estoque_lata_agua -= 1

                    print("\nLiberando o produto!")
                    print("Obrigado por comprar com a gente!\n")
                    print("---------------------------------")

            continuar = int(input("Deseja continuar com o programa? SIM(1) ou NÃO(2): "))
            while continuar != 1 and continuar != 2:
                continuar = int(input("Deseja continuar com o programa? SIM(1) ou NÃO(2): "))

            if continuar == 2:
                run_program = 0
    else:
        print("\n--------------------------------- \nSeja Bem-vindo ao modo Admin\n")
        if primeiro_uso == 1:
            senha_escolhida = int(input("Escolha uma senha com 6 números inteiros: "))
            senha_confirma = int(input("Confirme sua senha: "))
            while senha_escolhida != senha_confirma:
                print("Senha diferentes")
                senha_escolhida = int(input("Escolha uma senha com 6 números inteiros: "))
                senha_confirma = int(input("Confirme sua senha: "))
            primeiro_uso -= 1

        senha = int(input("Favor inserir senha de 6 dígitos escolhida: "))
        if senha != senha_escolhida:
            while tentativas > 0 and senha != senha_escolhida:
                print(f"Senha incorreta\nTentativas restantes: {tentativas}")
                senha = int(input("Favor inserir senha de 6 dígitos escolhida: "))
                tentativas -= 1

        if senha == senha_escolhida:
            print(f"Aqui segue o numero de moedas e cédulas de cada tipo:\nCédulas de 20 reais: {nota_20_caixa}\nCédulas de 10 reais: {nota_10_caixa}\nCédulas de 5 reais: {nota_5_caixa}\nCédulas de 2 reais: {nota_2_caixa}\nMoedas de 1 real: {moeda_1_caixa}\nMoedas de 50 centavos: {moeda_50_caixa}\nMoedas de 25 centavos: {moeda_25_caixa}\nMoedas de 10 centavos: {moeda_10_caixa}\nMoedas de 5 centavos: {moeda_5_caixa}")
            print(f"\nAqui segue o numero de latas em seu estoque:\nCoca-Cola: {estoque_lata_coca}\nRedBull: {estoque_lata_redbull}\nAgua: {estoque_lata_agua}")
            adicionar_latas = int(input("Deseja adicionar mais latas? Sim(1) ou Não(2): "))
            while adicionar_latas != 1 and adicionar_latas != 2:
                print("\nValor invalido, tente novamente")
                adicionar_latas = int(input("Deseja adicionar mais latas? Sim(1) ou Não(2): "))

            if adicionar_latas == 1:
                adicionar_latas_escolher = int(input("\n(1) Coca-Cola 350ml\n(2) RedBull 350ml\n(3) Água sem gas 500ml\nEscolha a bebida a estocar: "))
                while adicionar_latas_escolher != 1 and adicionar_latas_escolher != 2 and adicionar_latas_escolher != 3:
                    print("\nValor invalido, favor escolher uma das 3 opções!")
                    adicionar_latas_escolher = int(input("Escolha sua bebida (1|2|3)"))
                if adicionar_latas_escolher == 1:
                    adicionar_coca = int(input("Quantas latas de Coca-Cola você deseja adicionar? "))
                    while adicionar_coca <= 0:
                        print("Digite um número válido")
                        adicionar_coca = int(input("Quantas latas de Coca-Cola você deseja adicionar? "))

                    estoque_lata_coca += adicionar_coca
                    print(f"Novo estoque: {estoque_lata_coca} latas")

                if adicionar_latas_escolher == 2:
                    adicionar_RedBull = int(input("Quantas latas de RedBull você deseja adicionar? "))
                    while adicionar_RedBull <= 0:
                        print("Digite um número válido")
                        adicionar_RedBull = int(input("Quantas latas de RedBull você deseja adicionar? "))

                    estoque_lata_redbull += adicionar_RedBull
                    print(f"Novo estoque: {estoque_lata_redbull} latas")

                if adicionar_latas_escolher == 3:
                    adicionar_agua = int(input("Quantas latas de Água você deseja adicionar? "))
                    while adicionar_agua <= 0:
                        print("Digite um número válido")
                        adicionar_agua = int(input("Quantas latas de Água você deseja adicionar? "))

                    estoque_lata_agua += adicionar_agua
                    print(f"Novo estoque: {estoque_lata_agua} latas")

            valor_total_caixa = (nota_20_caixa * 20) + (nota_10_caixa * 10) + (nota_5_caixa * 5) + (nota_2_caixa * 2) + (moeda_1_caixa * 1) + (moeda_50_caixa * 0.50) + (moeda_25_caixa * 0.25) + (moeda_10_caixa * 0.10) + (moeda_5_caixa * 0.05)
            print(f"\nAqui segue o valor total do caixa: {valor_total_caixa}")

        continuar = int(input("Deseja continuar com o programa? SIM(1) ou NÃO(2): "))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Deseja continuar com o programa? SIM(1) ou NÃO(2): "))
        if continuar == 2:
            run_program = 0
