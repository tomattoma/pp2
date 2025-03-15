import re
#Напишите регулярное выражение для проверки корректности телефонного номера в формате +7-XXX-XXX-XX-XX.

text = input()
pattern = r"\+7-\d{3}-\d{3}-\d{2}-\d{2}$"

if re.fullmatch(pattern, text):
    print("Correct")
else:
    print("Wrong")