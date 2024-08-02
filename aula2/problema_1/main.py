"""
Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um
percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do
desconto e o preço final do produto

"""

price = float(input('Digite o preço do produto: '))
discount = float(input('Digite o desconto a aplicar: '))

discount_amount = float(price * (discount / 100))
new_price = float(price - discount_amount)

print(f'O preço inicial do produto é R$ {price}')
print(f'O desconto é de {discount}%')
print(f'O valor do desconto é R$ {discount_amount}')
print(f'O valor do produto com o desconto aplicado é R$ {new_price}')
