segundos = input("Por favor, entre com o número de segundos que deseja converter: ")

total_seg = int(segundos)

dias = total_seg // 86400
hora_rest = total_seg % 86400
horas = hora_rest // 3600
seg_rest = hora_rest % 3600
minutos = seg_rest // 60
seg_rest_f = seg_rest % 60

print("%s dias, %s horas, %s minutos e %s segundos."%(dias,horas,minutos,seg_rest_f))
