passing_grade = 7
test_grade1 = float(input('Digite a nota da prova 1: '))
test_grade2 = float(input('Digite a nota da prova 2: '))
test_grade3 = float(input('Digite a nota da prova 3: '))

if (test_grade1 >= passing_grade and test_grade2 >= passing_grade and
        test_grade3 >= passing_grade):
    print('Aprovado')
else:
    print('Reprovado')
