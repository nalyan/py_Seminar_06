# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму

n = int(input('input n: '))
print(sum(list(map(lambda x: (1+1/x)**x, list(i for i in range(1,n+1))))))