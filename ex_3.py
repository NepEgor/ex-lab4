#!/usr/bin/env python3

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3
sort = sorted(data, key=abs)  # key=lambda x: abs(x)
print(*sort, sep=', ')
