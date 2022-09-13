#内置函数Time
from ast import Str
import time
#时间戳 timestamp:time.time()
print(f'Now,the timestamp is : {time.time()}')

#格式化时间format string：time.strftime() ->string format time 的简写
print(f'Now the format string time is : {time.strftime("%Y-%m-%d %X")}')
#"%Y-%m-%d %X" 年月日连在一起，具体时间%X大学且分开

#结构化时间  九个元素年，月，日，时，分，秒，一年中第几周，一年中第几天，夏令时
print(f'Now the local time is : {time.localtime()}')
print(f'Now the UTC time is : {time.gmtime()}')
print(time.localtime(0))#基准时间
print(time.localtime(3600*24*365))
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
# time.struct_time(tm_year=1971, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=1, tm_isdst=0)


#三种时间方式的转换
struct_time = time.localtime()

time_stamp = time.mktime(struct_time)

time_format = time.strftime("%Y-%m-%d %X",struct_time)
struct_time1 = time.strptime(time_format, "%Y-%m-%d %X")
print(struct_time1)
print(struct_time)

print(struct_time,time_format,time_stamp)

#结构化时间格式化
print(time.asctime(time.localtime()))#最清晰的看法

start  = time.time()
time.sleep(3)
end = time.time()
lasting = (end - start)
print(lasting)









