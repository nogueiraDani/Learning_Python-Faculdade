# ---------------------------------------------------------------------------------------------------------------------
# 1.1 Evento de Teclado
import keyboard


def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:  # Verifica se a tecla foi pressionada
        print(f'Tecla pressionada: {event.name}')
        if event.name == 'a':
            print('a em especial')


#  main
keyboard.on_press(on_key_event)  # Registra o hook para o evento de tecla pressionada

# Mantém o programa em execução para capturar os eventos de tecla indefinidamente
try:
    while True:
        pass  # aqui eu poderia colocar o resto do meu código
except KeyboardInterrupt:
    print("Programa interrompido pelo usuário.")