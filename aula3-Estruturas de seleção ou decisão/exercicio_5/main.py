apple_price = 2.30
orange_price = 3.60
banana_price = 1.85

selected_option = int(input('Quais frutas deseja comprar: 1-maçã | 2-laranja '
                            '| 3-banana : '))
final_price = 0

if selected_option != 1 and selected_option != 2 and selected_option != 3:
    print('Produto inexistente.')
else:
    amount = int(input('Quantas unidades deseja comprar: '))
    if selected_option == 1:
        final_price = float(amount * apple_price)
        print(f'Você comprou {amount} maçã(s).')
    elif selected_option == 2:
        final_price = float(amount * orange_price)
        print(f'Você comprou {amount} laranja(s).')
    elif selected_option == 3:
        final_price = float(amount * banana_price)
        print(f'Você comprou {amount} banana(s).')

print(f'Valor final da compra: R$ {final_price}')
