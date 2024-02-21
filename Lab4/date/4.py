import datetime
date1 = datetime.datetime(2023, 5, 6, 8, 45, 0)  
date2 = datetime.datetime(2024, 2, 21, 12, 17, 15)
difference = date2 - date1
seconds = difference.total_seconds()
print(seconds)
