# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


a = int(input("Введите трехзначное число: "))
print((a % 10) + (a % 100)//10 + (a // 100))












