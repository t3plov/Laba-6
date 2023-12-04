import sys
import random

try:
    n = int(input("Введите кол-во элементов списка: "))
    if n < 1:
        print("Неправильное кол-во элементов")
        sys.exit()
    a = [0] * n
    for i in range(n):
        a[i] = random.randint(-1000, 1000)
    count = 0
    ind = 0
    mini = 100000
    summ = 0
    print(a)
    for i in range(n):
        if a[i] == 0:
            count += 1
        if a[i] < mini:
            ind = i
    print("Кол-во нулей в списке: ", count)
    for i in range(ind+1, n):
        summ += a[i]
    print("Сумма элементов после минимального: ", summ)
except ValueError:
    print("Неправильное значение.")
