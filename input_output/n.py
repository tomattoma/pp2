n = int(input())

start_time = 9 * 60  
lesson_duration = 45 

short_breaks = (n - 1) // 2 * 5  


long_breaks = (n // 2) * 15  

total_time = start_time + n * lesson_duration + short_breaks + long_breaks


hours = total_time // 60
minutes = total_time % 60

print(hours, minutes)