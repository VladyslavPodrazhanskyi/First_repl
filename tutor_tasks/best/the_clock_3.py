# С начала суток часовая стрелка повернулась
# на угол в α градусов. Определите сколько полных
# часов, минут и секунд прошло с начала суток,
# то есть решите задачу, обратную задаче «Часы - 1». Запишите ответ в три переменные и выведите их на экран.

h_angle = float(input())
# total_hours = h_angle * 12 / 360 = h_angle / 30
# hours = int(total_hours)
total_seconds = h_angle*120
# hours = total_seconds // 3600
hours = h_angle // 30
left_from_hours = total_seconds - hours * 3600
minutes = left_from_hours // 60
seconds = int(left_from_hours % 60)


print(hours, minutes, seconds)
