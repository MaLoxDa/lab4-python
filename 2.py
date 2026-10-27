# Задание2
import math

print("Разложение sin(x) через бесконечное произведение")
print("Формула: sin(x) = x * (1 - x^2/pi^2) * (1 - x^2/(4pi^2)) * ...")

x = float(input("Введите x (например, 0.5): "))
eps = float(input("Введите точность eps (например, 0.0001): "))

left = math.sin(x)   
right = x            
n = 2               

while abs(left - right) > eps:
    # знаменатель
    k = n - 1
    znamenatel = (k * k) * (math.pi * math.pi)
    
    # домнож 1части на скобку
    right = right * (1 - (x * x) / znamenatel)
    
    # след множитель
    n = n + 1

print("sin(x) стандартный:      ", left)
print("sin(x) через произведение:", right)
print("Разница:                  ", abs(left - right))
print("Понадобилось множителей:  ", n - 2)