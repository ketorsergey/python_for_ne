# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

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
        if "interface" and "Ethernet" in line and "switchport mode access" in cfg_list[i + 1] and "switchport access vlan" not in cfg_list[i + 2]:
            access_interfaces.append(line.split()[1])
            access_vlans.append(1)
        elif "interface" and "Ethernet" in line and "switchport mode access" in cfg_list[i + 1] and "switchport access vlan" in cfg_list[i + 2]:
            access_interfaces.append(line.split()[1])
            access_vlans.append(cfg_list[i + 2].split()[3])
        elif "interface" and "Ethernet" in line and "switchport trunk encapsulation" in cfg_list[i + 1]:
            trunk_interfaces.append(line.split()[1])
            trunk_vlans.append(cfg_list[i + 2].split()[4].split(','))
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
