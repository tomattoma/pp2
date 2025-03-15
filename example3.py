#найти все слова начинающиеся с заглавной буквы
import re

your_email = input()
pattern = r"\b[A-Z][a-z]+\b"

emails = re.findall(pattern, your_email)
print(emails)