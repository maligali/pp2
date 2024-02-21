import datetime
current = datetime.datetime.now()
without = current - datetime.timedelta(microseconds=current.microsecond)
print(without)
