def to_divide():
    try:
        number1 = float(input('Digite o primeiro número: '))
        number2 = float(input('Digite o segundo número: '))
        result = number1 / number2
    except ZeroDivisionError:
        print(f'Erro, número {number1} não pode ser divido por 0 ('
              f'{number2})')
    except ValueError:
        print('Você deve digitar somente números.')
    else:
        return round(result, 2)
    finally:
        print('Mensagem fixa')


print(to_divide())

