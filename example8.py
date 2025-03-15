import re
#Напишите регулярное выражение, которое находит даты в тексте в формате DD.MM.YYYY.

text = input()

pattern = r"\b\d{2}\.\d{2}\.\d{4}\b"

if re.search(pattern, text):
    print("YES")
else:
    print("NO")