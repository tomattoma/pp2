from datetime import datetime
#Write a Python program to calculate two date difference in seconds.

first = input()
second = input()

date1 = datetime.strptime(first, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(second, "%Y-%m-%d %H:%M:%S")

difference = abs((date2-date1).total_seconds())

print(difference)