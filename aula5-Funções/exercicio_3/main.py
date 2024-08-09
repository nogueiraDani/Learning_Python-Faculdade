def realce(text):
    size = len(text)
    if size:
        print('+', '-' * size, '+')
        print('|', text, '|')
        print('+', '-' * size, '+')


realce('DANIELA')
realce('TATI')

