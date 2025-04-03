def omelete():
    global ovos # => torna a variavel local em global
    ovos = 6


ovos = 12
omelete()
print(ovos)

