# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_add = input("Введите IP-адрес в формате 10.0.1.1: ")


ip_ok = False

while ip_ok == False:
    octets = ip_add.split(".")
    if len(octets) != 4:
       print('Неправильный IP-адрес')
       ip_add = input("Введите IP-адрес в формате 10.0.1.1: ")
    elif not octets[0].isdigit() or not octets[1].isdigit() or not octets[2].isdigit() or not octets[3].isdigit():
       print('Неправильный IP-адрес')
       ip_add = input("Введите IP-адрес в формате 10.0.1.1: ")
    elif not int(octets[0]) in range(0, 256) or not int(octets[1]) in range(0, 256) or not int(octets[2]) in range(0, 256) or not int(octets[3]) in range(0, 256):
       print('Неправильный IP-адрес')
       ip_add = input("Введите IP-адрес в формате 10.0.1.1: ")
    else:
        ip_ok = True


while ip_ok == True:
    octets = ip_add.split(".")
    if int(octets[0]) in range(1, 224):
        print("unicast")
        break
    elif int(octets[0]) in range(224, 240):
        print("multicast")
        break
    elif ip_add == "255.255.255.255":
        print("local broadcast")
        break
    elif ip_add == "0.0.0.0":
        print("unassigned")
        break
    else:
        print("unused")
        break
