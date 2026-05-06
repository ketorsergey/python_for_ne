# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    command_output_list = command_output.rstrip().split('\n')
    
    data_begin = 0
    hostname = ""
    
    for position, string in enumerate(command_output_list,0):
        if string.startswith('Device'):
            data_begin = position + 1
        elif ">" in string:
            hostname = string.split(">")[0]
        else:
            continue
            
    data_list = command_output_list[data_begin:]
    cleaned_data_list = []
    
    for position, string in enumerate(data_list,0):
        list_from_str = string.split("  ")
#        print(list_from_str )
        temp_list = []
        for elem in list_from_str:
            if elem == "":
                continue
            elif len(elem)> 7:
                temp_list.append(elem.strip().replace(' ', '')[elem.strip().replace(' ', '').find("Eth"):])
            elif "th" in elem:
                temp_list.append(elem.strip().replace(' ', ''))
            elif "R S I" in elem:
                continue
            else:
                temp_list.append(elem.strip())
                
        cleaned_data_list.append(temp_list)
    
    for data in cleaned_data_list:
        data.pop(2)
    for data in cleaned_data_list:
        data.pop(2)
    for data in cleaned_data_list:
        data.append(hostname)
    for data in cleaned_data_list:
        data[-1], data[0] = data[0], data[-1]
    for data in cleaned_data_list:
        data[-1], data[2] = data[2], data[-1]
        
#    print(cleaned_data_list)
    
    d_keys = []
    d_values = []
        
    for elem_list in cleaned_data_list:
        keys = []
        values = []
        keys.append(elem_list[0])
        keys.append(elem_list[1])
        values.append(elem_list[2])
        values.append(elem_list[3])
        d_keys.append(tuple(keys))
        d_values.append(tuple(values))

#    print(d_keys)
#    print(d_values)
    
    result = dict(zip(d_keys, d_values))
    
    return result
    
if __name__ == "__main__":
    with open("sh_cdp_n_r2.txt") as f:
        print(parse_cdp_neighbors(f.read()))
        
infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

