# Лабораторная №1 задание 3 вариант 5
# Дана непустая последовательность ненулевых целых чисел, за которой следует 0.
# Определить, сколько раз в этой последовательности меняется знак.
A = []
a = int(input("Введиде первое целое число:\n"))
A.append(a)
k = 0
if a != 0:
    b = int(input("Введите следующее целое число:\n"))
    while b != 0:
           if abs(a + b) != (abs(a) + abs(b)):
            k = k + 1
            a = b
            A.append(a)
            b = int(input("Введите следующее целое число:\n"))
           else:
                k = k + 0
                a = b
                b = int(input("Введите следующее число:\n"))
                A.append(a)
    print("Был введен ноль ")
    print("Введеная последовательность ", A)
    print("Столько раз в последовательности менялся знак =", k)
else:
    print("Был введен ноль ")
