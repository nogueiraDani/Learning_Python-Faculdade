"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro
lugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi
alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e
R$ 0,15 por km rodado

"""

car_value_per_day = 60
car_value_per_km = 0.15
km_traveled = float(input('Informe a quantidade de kilômetros percorridos: '))
days_traveled = float(input('Informe a quantidade de dias alugados: '))

amount_to_pay = (car_value_per_day * days_traveled) + (car_value_per_km *
                                                        km_traveled)

print(f'Valor a pagar R$ {amount_to_pay}')
