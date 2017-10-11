#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1]
data2 = gen_random(1, 3, 10)
data3 = ['ABC', 'aBc', 'AbC']

# Реализация задания 2
uni1 = Unique(data1)
print(*uni1, sep=', ')

uni2 = Unique(data2)
print(*uni2, sep=', ')

uni31 = Unique(data3)
uni32 = Unique(data3, ignore_case=True)
print(*uni31, sep=', ')
print(*uni32, sep=', ')
