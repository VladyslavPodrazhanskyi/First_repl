import datetime

now = datetime.datetime.now()
print(datetime.date.today())
print(type(datetime.date.today()))
print(now.strftime("%Y %m %d %H %M %s"))
print(type(now.strftime("%Y %m %d %H %M %s")))