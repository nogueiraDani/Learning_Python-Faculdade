def calculate_factorial(num):
    """
    Função para calcular o fatorial de um valor
    :param num: número a calcular
    :return: fatorial calculado
    """

    amout = 1
    if validate_positive_number(num):
        if num == 0 or num == 1:
            return amout
        else:
            for i in range(1, num + 1, 1):
                amout *= i
        return amout
    else:
        return 'O número deve ser positivo.'


def validate_positive_number(num):
    """
    Função para validar se numero digitado é positivo
    :param num: valor a validar
    :return: resposta true ou false
    """

    if num >= 0:
        return True
    else:
        return False


question = int(input('Digite um valor para calcular o fatorial: '))
print(f'{question}! = {calculate_factorial(question)}')


help(calculate_factorial)