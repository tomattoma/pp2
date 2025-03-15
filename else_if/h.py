x1 = int(input())  
y1 = int(input())  
x2 = int(input())  
y2 = int(input())  

# Слон бьёт, если разница по горизонтали равна разнице по вертикали
if abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")