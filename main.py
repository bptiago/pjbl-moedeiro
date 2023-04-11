# Coisas que precisa implementar:
# Cenários para quando o comando não corresponder a nenhum produto
# Troco
# Sistema de administrador

print('MÁQUINA DE REFRIGERANTE')
print('---------------------------------')
print('(1) Coca-Cola 350ml - R$5,00')
print('---------------------------------')

comando = int(input('Digite o número do produto que você deseja: '))
print('---------------------------------')
if comando == 1:
    valor_produto = 5
    valor_inserido = float(input('Insira o dinheiro aqui: '))
    print('---------------------------------')

    if valor_inserido < valor_produto:
        print('Saldo insuficiente!')
        print('Deseja adicionar mais dinheiro?')
        escolha = 0
        print('---------------------------------')

        # Evitar opções inexistentes
        while escolha != 1 and escolha != 2:
            escolha = int(input('Pressione 1 para SIM e 2 para NÃO: '))
            if escolha != 1 and 2:
                print('Digite uma opção válida!')
            print('---------------------------------')

        # Adição de mais saldo
        # A variável valor_inserido vai ser usada depois para terminar a compra e calcular o troco
        if escolha == 1:
            valor_adicionado = float(input('Insira a quantidade de dinheiro que gostaria de adicionar: '))
            valor_inserido = valor_inserido + valor_adicionado
            print('Agora você possui um total de R$', valor_inserido)
            # Assim que esse valor_inserido é atualizado, ele pula para o bloco de if seguinte.

        # Cancelamento de transação
        else:
            print('Transação cancelada!')
            print('Devolvendo seu dinheiro')

    if valor_inserido >= valor_produto:
        print('---------------------------------')
        print('Completando a transação')
        # Precisa fazer a parte do troco
