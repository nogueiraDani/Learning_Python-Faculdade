print('-' * 3, '| Lanchonete |', '-' * 3)
print('-' * 22)
print('-' * 6, '| MENU |', '-' * 6)
print('-|', '1-coxinha', 'R$5,00', '|-')
print('-|', '2-pastel', 'R$7,00 ', '|-')
print('-|', '3-café', 'R$4,00   ', '|-')
print('-|', '4-suco', 'R$6,00   ', '|-')
print('-|', '5-sair', '          |-')
print('-' * 22)

amount = 0

while True:
    try:
        option = int(input('\nQual item deseja comprar? '))

        if option == 1:
            quantity = int(input('Quantos itens deseja comprar? '))
            amount += amount + quantity * 5
        elif option == 2:
            quantity = int(input('Quantos itens deseja comprar? '))
            amount += amount + quantity * 7
        elif option == 3:
            quantity = int(input('Quantos itens deseja comprar? '))
            amount += amount + quantity * 4
        elif option == 4:
            quantity = int(input('Quantos itens deseja comprar?'))
            amount += amount + quantity * 6
        elif option == 5:
            print(f'O seu pedido ficou R$ {format(amount, ".2f")}')
            break
        else:
            print('Digite uma opção de 1 a 5')

    except ValueError:
        print('Digite somente números')




