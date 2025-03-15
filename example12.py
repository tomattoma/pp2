import re
#Write a Python program to split a string at uppercase letters.
text = input()
res = re.findall(r"[A-Z][a-z]*", text)
print(res)