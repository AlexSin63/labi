# Лабораторная работа № 2 с методами сортировки Select и Shell
import random
import datetime
import prettytable
import matplotlib.pyplot as plt

def SelectionSort(A): # сортировка Select
    n = len(A)
    i = 0
    while i < n -1:
        smal = i
        j = i + 1
        while j < n :
            if A[j] < A[smal]:
                smal = j
            j+=1
        A[i], A[smal] = A[smal], A[i]
        i+=1
    return

def ShellSort(B):       # сортировка SHell
    t = int(len(B)/2)
    while t > 0:
        for i in range(len(B)-t):
            j = i
            while j >= 0 and B[j] > B[j+t]:
                B[j], B[j+t] = B[j+t], B[j]
                j-= 1
        t = int(t/2)

table=prettytable.PrettyTable(["Размер списка","Время Select", "Время Shell"])
x =[]
y1=[]
y2=[]

for N in range(1000,10000,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range(N):
        A.append(int(round(random.random()*(max-min)+min)))
    B = A.copy()
    print("---------------------------------------------")

    t1 = datetime.datetime.now()
    SelectionSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Сортировка Select  " + str(N) +" заняла " + str((t2-t1).total_seconds()) + " с")

    t3 = datetime.datetime.now()
    ShellSort(B)
    t4 = datetime.datetime.now()
    y2.append((t4-t3).total_seconds())
    print("Сортировка Shell   " + str(N) + " занялa "+ str((t4-t3).total_seconds()) + " с")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C3")
plt.show()
