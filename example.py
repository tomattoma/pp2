import re

your_email = input()
pattern = r"[a-zA-z0-9._]+@[a-z]+\.[a-z]{2,}"

if(re.search(pattern,your_email)):
    print("Everything is good")
else:
    print("Wrong email!\nPleas repeat it")