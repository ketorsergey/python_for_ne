# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    
    f = open(config_filename)
    cfg_list = f.read().split('\n')

    access_interfaces = []
    access_vlans = []
        
    trunk_interfaces = []
    trunk_vlans = []
    
    i = 0
    for line in cfg_list:
        if "interface" and "Ethernet" in line and "switchport mode access" in cfg_list[i + 1]:
            access_interfaces.append(line.split()[1])
        elif "interface" and "Ethernet" in line and "switchport trunk encapsulation" in cfg_list[i + 1]:
            trunk_interfaces.append(line.split()[1])
        elif "switchport access vlan" in line:
            access_vlans.append(line.split()[3])
        elif "trunk allowed vlan" in line:
            trunk_vlans.append(line.split()[4].split(',')) 
        i += 1  
    f.close()
    
    int_trunk_vlans = []
    for vlans in trunk_vlans:
        int_vlans = []
        for vlan in vlans:
            int_vlans.append(int(vlan))
        int_trunk_vlans.append(int_vlans)
    
    access_result = dict.fromkeys(access_interfaces)
    i = 0
    for key in access_result:
        access_result[key] = int(access_vlans[i])
        i += 1
    
    trunk_result = dict.fromkeys(trunk_interfaces)
    i = 0
    for key in trunk_result:
        trunk_result[key] = int_trunk_vlans[i]
        i += 1
    
    result = (access_result, trunk_result)

    return(result)
