# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
user_input = int(input('Enter VLAN number: '))

f = open('CAM_table.txt')

f_list = []

for line in f:
    if len(line.split()) == 4 and line.split()[0].isdigit():
        f_list.append(line.split())
    else:
        continue

i = 0
for elems in f_list:
    f_list[i][0] = int(f_list[i][0])
    i +=1


for line in f_list:
    if line[0] == user_input:
        print("{:<9}{:<20}{:<4}".format(line[0], line[1], line[3]))
    else:
        continue

f.close()
