#!/usr/bin/env python3
from librip.gens import *

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1

print(*field(goods, 'title'), sep=', ')
print(*field(goods, 'title', 'price'), sep=', ')
print(*field(goods, 'title', 'price', 'color'), sep=', ')

print(*gen_random(1,20,5), sep=', ')
