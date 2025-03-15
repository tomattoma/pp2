a = int(input())
b = int(input())
n = int(input())

rub = a*n
cop = b*n

if cop > 99:
    rub+=cop//100
    cop%=100

print(rub, cop)