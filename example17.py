from datetime import datetime, timedelta
#Write a Python program to subtract five days from current date.

now = datetime.now()
day = timedelta(days=5)
result = now - day
print(result)