total_seg = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = total_seg // 86400
seg_restantes = total_seg % 86400
horas = seg_restantes // 3600
seg_restantes2 = seg_restantes % 3600
minutos = seg_restantes2 // 60
ultimos_segundos = seg_restantes2 % 60

print('{} dias, {} horas, {} minutos e {} segundos.'.format(dias, horas, minutos, ultimos_segundos))