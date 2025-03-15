import re
#Напишите программу, которая проверяет, является ли введенная строка корректным email-адресом.

text = input()

pattern =  r"^[a-zA-z0-9._]+@[a-z]+\.(com|net|ru|edu|kz)$"

if re.search(pattern,text):
    print("YES")
else:
    print("NO")