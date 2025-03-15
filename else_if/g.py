x1 = int(input())  
y1 = int(input())  
x2 = int(input())  
y2 = int(input())  

# Ладья бьёт, если либо координаты строк совпадают, либо координаты столбцов
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")