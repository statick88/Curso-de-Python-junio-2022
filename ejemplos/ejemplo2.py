minutes_worked = int(input('Total de minutos: '))

HOURS = 60  # 60 minute

WORKS_DAYS = 20  # 4 week * 5 days

work_hours = (minutes_worked // HOURS) // WORKS_DAYS

print(work_hours, 'horas por días')