import re
#Write a Python program to convert a given camel case string to snake case.
def snake_case(text):
    text = re.sub(r"([a-z])([A-Z])", r"\1_\2", text)
    return text.lower()

CamelText = input()
print(snake_case(CamelText))