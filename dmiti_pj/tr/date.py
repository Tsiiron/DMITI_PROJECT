import calendar
year = 2023 
month = 3 
num_days = calendar.monthrange(year, month)[1]
print(f"There are {num_days} days in {calendar.month_name[month]}, {year}")