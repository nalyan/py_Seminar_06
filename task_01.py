# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('input number: ');
print(sum([int(i) for i in number if i.isdigit()]))
