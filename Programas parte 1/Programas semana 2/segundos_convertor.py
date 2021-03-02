segundos_str = input("Por favor, entre com o numero de segundos: ")
total_segs = int(segundos_str)

dias = total_segs // 86400
horas_restantes = total_segs // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias, "Dias, ", horas_restantes, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos.")

