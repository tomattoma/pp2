import re

your_email = input()
pattern = r"[a-zA-z0-9._]+@[a-z]+\.[a-z]{2,}"

emails = re.findall(pattern, your_email)
print(emails)