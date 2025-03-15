import re
#Write a python program to convert snake case string to camel case string. 
def CamelCase(text):
    if not text:
        return ""
    
    def upper_f(match):
        return match.group(1).upper()
    
    text = re.sub(r"_+(\w)", upper_f, text.lower())

    return text[0].upper() + text[1:]

snake_case = input()
print(CamelCase(snake_case))
