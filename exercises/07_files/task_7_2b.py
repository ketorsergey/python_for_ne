# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]

file_r = open(argv[1], "r")
file_w = open(argv[2], "w")


for line in file_r:
    if "!" in line or ignore[0] in line or ignore[1] in line or ignore[2] in line:
        continue
    else:
        file_w.write(line)
        
file_r.close()
file_w.close()
