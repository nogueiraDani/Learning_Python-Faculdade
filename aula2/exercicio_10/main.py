"""
-Escreva as seguintes atribuições:
--s1 = 'ant'
--s2 = 'bat'
--s3 = 'cod'

apresentar as seguintes saidas, usando + e *
'ant bat cod'
'ant ant ant ant ant ant ant ant ant ant'
'ant bat bat cod cod cod'
'ant bat ant bat ant bat ant bat'
'batbatcod batbatcod batbatcod batbatcod batbatcod'

"""

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

print(s1, s2, s3) #'ant bat cod'
print(f'{s1} ' * 10) #'ant ant ant ant ant ant ant ant ant ant '
print(f'{s1} ' + f'{s2} ' * 2 + f'{s3} ' * 3) # 'ant bat bat cod cod cod '
print(f'{s1} {s2} ' * 4) # 'ant bat ant bat ant bat ant bat '
print(f'{s2 * 2}{s3} ' * 5) # 'batbatcod batbatcod batbatcod batbatcod batbatcod '