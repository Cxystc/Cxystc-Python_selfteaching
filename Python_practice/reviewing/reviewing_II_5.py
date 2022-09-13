#datetime 
import datetime
import time
print(datetime.datetime.now())
print(datetime.date.fromtimestamp(time.time()))
print(datetime.datetime.now() + datetime.timedelta(3))
print(datetime.datetime.now() + datetime.timedelta(-3))
print(datetime.datetime.now() + datetime.timedelta(hours = 3))
print(datetime.datetime.now() + datetime.timedelta(minutes =3 ))#注意要加s : hours minutes seconds

now_time = datetime.datetime.now()
print(now_time.replace(hour=5, minute = 20 ,second = 1))#注意这里是没有s的minute hour second




