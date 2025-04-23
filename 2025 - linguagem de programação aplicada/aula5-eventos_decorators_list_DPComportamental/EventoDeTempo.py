
# 1.2 Evento de Tempo
import sched #agenda eventos
import time


def exibir_mensagem(mensagem):
    print(mensagem)


def agendar_evento(scheduler, intervalo, mensagem):
    # Agendando o próximo evento
    scheduler.enter(intervalo, 1, agendar_evento, (scheduler, intervalo, mensagem))

    # Exibindo a mensagem
    exibir_mensagem(mensagem)


# Cria uma instância do objeto scheduler
new_scheduler = sched.scheduler(time.time, time.sleep)

# Agendando o primeiro evento
agendar_evento(new_scheduler, 1, "Esta é a mensagem agendada a cada 1 segundo!")

print("Esperando para exibir as mensagens agendadas...")

# Executando o scheduler em loop (Ctrl + F2 para interromper manualmente) devido ao evento de tempo, sem main
new_scheduler.run()
# ---------------------------------------------------------------------------------------------------------------------
