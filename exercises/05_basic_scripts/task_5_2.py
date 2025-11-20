# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
address = input("Введите сеть x.x.x.x/y :")

ip = address.split("/")[0].split(".")
mask = address.split("/")[1]

ip_template = """
Network:
{:<8}  {:<8}  {:<8}  {:<8}
{:08b}  {:08b}  {:08b}  {:08b}
"""

print(ip_template.format(ip[0], ip[1], ip[2], ip[3], int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])))

mask_template = """
Mask:
/{}
{:<8}  {:<8}  {:<8}  {:<8}
{:08b}  {:08b}  {:08b}  {:08b}
"""

mask_str = int(mask) * "1" + (32 - int(mask))* "0"

mask_oct1 = mask_str[0:8]
mask_oct2 = mask_str[8:16]
mask_oct3 = mask_str[16:24]
mask_oct4 = mask_str[24:]

int_mask_oct1 = int(mask_oct1, 2)
int_mask_oct2 = int(mask_oct2, 2)
int_mask_oct3 = int(mask_oct3, 2)
int_mask_oct4 = int(mask_oct4, 2)

print(mask_template.format(mask, int_mask_oct1, int_mask_oct2, int_mask_oct3, int_mask_oct4, int_mask_oct1, int_mask_oct2, int_mask_oct3, int_mask_oct4))
