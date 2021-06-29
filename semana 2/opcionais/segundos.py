segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos//86400
segundosr = segundos % 86400
horas = segundosr // 3600
segundosr = segundosr % 3600
minutos = segundosr // 60
segundosr = segundosr % 60

print(dias, "dias,", horas, "horas,", minutos,"minutos e", segundosr, "segundos")
