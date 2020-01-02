#В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты. За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.

pupils_1 = int(input('Input number of pupils in the class 1: '))
pupils_2 = int(input('Input number of pupils in the class 2: '))
pupils_3 = int(input('Input number of pupils in the class 3: '))

desks_1 = (pupils_1 // 2) + (pupils_1 % 2)
desks_2 = (pupils_2 // 2) + (pupils_2 % 2)
desks_3 = (pupils_3 // 2) + (pupils_3 % 2)

totals_desks = desks_1 + desks_2 + desks_3
print(totals_desks)