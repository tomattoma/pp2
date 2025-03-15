x1 = int(input())  
y1 = int(input())  
x2 = int(input())  
y2 = int(input())  

# Король может ходить на 1 клетку в любом направлении:
# Разница по горизонтали и вертикали не должна превышать 1
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print("YES")
else:
    print("NO")