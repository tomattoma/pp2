n = int(input())
m = int(input())

print((n % m != 0 and m & n != 0)+1)
print(1 + (n % m > 0) * (m % n > 0))