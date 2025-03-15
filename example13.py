import re
#Write a Python program to insert spaces between words starting with capital letters

text = input()
new_text = re.sub(r"([a-z])([A-Z])",r"\1 \2", text)
print(new_text)