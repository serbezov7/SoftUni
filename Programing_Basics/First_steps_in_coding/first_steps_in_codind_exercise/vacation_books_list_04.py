pages = int(input())
pages_per_hour = int(input())
days = int(input())

time_for_book = pages // pages_per_hour
hours_per_day = time_for_book // days
print(hours_per_day)
