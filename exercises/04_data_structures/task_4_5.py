# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов, которые есть
и в команде command1 и в команде command2 (пересечение).

В данном случае, результатом должен быть такой список: ['1', '3', '8']

Записать итоговый список в переменную result. (именно эта переменная будет
проверяться в тесте)

Полученный список result вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

vlan_list_1 = command1.split()[-1].split(",")
vlan_list_2 = command2.split()[-1].split(",")

set1 = set(vlan_list_1)
set2 = set(vlan_list_2)
unique_list = list(set2 & set1)

unique_list_int = [int(value) for value in unique_list]
unique_list_int.sort()

result = []
for item in unique_list_int:
    result.append(str(item))

print(result)
