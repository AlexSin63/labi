# Лабораторная №1 задание 2 вариант 5 (2)
import math
import numpy
# исходные данные
x = -1
k = 6
i = numpy.arange(0, 3.5, 0.5)
y = 1.6**-4
print("i", i)
# вычисления
c = []
d = []
n = 0
while n < len(i):
    c.append((i[n] / k) - math.sqrt(y) / 0.4)
    d.append((math.exp(1 - c[n])) + 4.9 * (x ** 2 + 1))
    n = n + 1
print("Ввывод значений c (while):",(c))
print("Ввывод значений d (while):", (d))
