x1 = int(input())  
y1 = int(input())  
x2 = int(input())  
y2 = int(input())  

# Ферзь бьёт, если:
# 1. Стоит на той же строке (горизонтальный ход)
# 2. Стоит в том же столбце (вертикальный ход)
# 3. Ходит по диагонали (разница по строкам = разница по столбцам)
if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")