import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print(yesterday.strftime("%Y-%M-%D"))
print(today.strftime("%Y-%M-%D"))
print(tomorrow.strftime("%Y-%M-%D"))