def square(num):
    return num**2

mylist = list(map(int, input().split()))
myiter = iter(mylist)

print(square(next(myiter)))  
print(square(next(myiter)))
print(square(next(myiter)))

