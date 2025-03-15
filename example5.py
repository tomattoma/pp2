import re

text = input()
pattern = r"[A-Z][0-9]{3}[A-Z]{2}[0-9]{2,3}$"

if re.fullmatch(pattern,text):
    print("Correct")
else:
    print("Error")
