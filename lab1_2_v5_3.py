# Лабораторная №1 задание 2 вариант 5 (3)
import math
import numpy
#исходные данные
k = 6
i = 8
y = [1.3, 8, 0.2]
x = numpy.arange(1, 2.1, 0.1)
#вычисления
c =[]
d =[]
for n in range(len(y)):
    c.append((i / k) - math.sqrt(y[n]) / 0.4)
    for m in range(len(x)):
        d.append(math.exp(1 - c[n]) + 4.9 * (x[m] ** 2 + 1))
print("Ввывод значений  функции c :", c)
print("Длина d =", len(d), "элемента. \n Ввывод значений функции d :", d)
