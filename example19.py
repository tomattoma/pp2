from datetime import datetime, timedelta
#Write a Python program to drop microseconds from datetime.

today = datetime.now()

result = today.strftime("%Y-%m-%d %H:%M:%S")
print(result)