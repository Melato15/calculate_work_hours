from datetime import datetime, timedelta
def CalcularHorasTrabalhadas(inicio: str, saida: str, almoco: str):
  inicio = input("Insira o horário de inicio (hhmm): ")
  saida = input("Insira o horário que você sai (hhmm): ")
  almoco = input("Insira seu tempo de almoço (hhmm): ")

  horario_inicio = datetime.strptime(inicio[:2] + ':' + inicio[2:], '%H:%M')
  horario_saida = datetime.strptime(saida[:2] + ':' + saida[2:], '%H:%M')
  horario_almoco = datetime.strptime(almoco[:2] + ':' + almoco[2:], '%H:%M')

  tempo_almoco = timedelta(hours=horario_almoco.hour, seconds=horario_almoco.second)

  horas_trabalhadas = abs(horario_saida - horario_inicio)

  horas_trabalhadas -= tempo_almoco

  print(horas_trabalhadas.seconds // 3600)