#Дано два числа a и b. Найдите гипотенузу треугольника с заданными катетами.
import math

a = float(input())
b = float(input())

c = math.sqrt(a**2 + b**2)
print(f"{c:.6f}")