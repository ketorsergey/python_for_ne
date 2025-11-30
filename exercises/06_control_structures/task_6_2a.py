# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_add = input("Введите IP-адрес в формате 10.0.1.1: ")

octets = ip_add.split(".")

ip_ok = True


if len(octets) == 4:
    for num in octets:
        if not num.isdigit():
            print('Неправильный IP-адрес')
            ip_ok = False
            break
            
        elif int(num) not in range(0, 256):
            print('Неправильный IP-адрес')
            ip_ok = False
            break
else:
    print('Неправильный IP-адрес')
    ip_ok = False
    
        
while ip_ok == True:
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
