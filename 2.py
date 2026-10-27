# Задание2
import math

print("Разложение sin(x) через бесконечное произведение")
print("sin(x) = x * (1 - x^2/pi^2) * (1 - x^2/(4pi^2)) * ...")

x = float(input("Введите x (например, 0.5): "))
eps = float(input("Введите точность eps (например, 0.0001): "))

left = math.sin(x)          
right = x                   
n = 1                       

while abs(left - right) > eps:
    right = right * (1 - x * x / (n * n * math.pi * math.pi))
    n = n + 1

print("sin(x) стандартный:     ", left)
print("sin(x) через произведение:", right)
print("Разница:                 ", abs(left - right))
print("Понадобилось множителей: ", n - 1)