# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

template = {
    'access': {
        "switchport mode access" : None,
        "switchport access vlan {}" : None,
        "switchport nonegotiate" : None,
        "spanning-tree portfast" : None,
        "spanning-tree bpduguard enable" : None,
            },
    'trunk': {
        "switchport trunk encapsulation dot1q" : None,
        "switchport mode trunk" : None,
        "switchport trunk allowed vlan {}" : None,
            }
        }
        
template_2 = {'access': "Введите номер VLAN:", 'trunk': 'Введите разрешенные VLANы:'}
        

intf_mode = input("Введите режим работы интерфейса (access/trunk): ")
intf_type = input("Введите тип и номер интерфейса: ")
intf_vlan = input(template_2[intf_mode])


print("interface " + intf_type, str(list(template[intf_mode].keys())).strip('[]').replace(', ', '\n').replace("'", '').format(intf_vlan), sep='\n')
