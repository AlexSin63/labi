# Лабораторная №1 задание 2 вариант 5 (1)

import math
import numpy
# исходные данные
x = -1
k = 6
i = (0.9, 8, 4, 2)
y = 1.6**-4

# вычисления
c = []
d = []
for n in range(len(i)):
    c.append((i[n] / k) - math.sqrt(y) / 0.4)
for m in range(len(c)):
    d.append (math.exp(1 - c[m]) + 4.9 * (x ** 2 + 1))
print("Ввывод значений c (for):",(c))
print("Ввывод значений d (for):", (d))

