from datetime import datetime, timedelta
#Write a Python program to print yesterday, today, tomorrow.

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(yesterday)
print(today)
print(tomorrow)
