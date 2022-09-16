#logging模块
import logging
#简单了解一下logging
logging.debug("debug info")
logging.info("正常信息")
logging.warning("warnign info")
logging.error("error info")
logging.critical("critical info")
#默认的级别是warning所以warning及以上才会显示

logging.basicConfig(filename = 'testinglogging.lg',format = '%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s',
datefmt = '%Y-%m-%d %H:%M:%S',
level = 10)

logging.debug('调试信息')  # 10
logging.info('正常信息')  # 20
logging.warning('警告信息')  # 30
logging.error('报错信息')  # 40
logging.critical('严重错误信息')  # 50
# %(name)s Logger的名字
# %(levelno)s 数字形式的日志级别
# %(levelname)s 文本形式的日志级别
# %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s 调用日志输出函数的模块的文件名
# %(module)s 调用日志输出函数的模块名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
# %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
# %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d 线程ID。可能没有
# %(threadName)s 线程名。可能没有
# %(process)d 进程ID。可能没有
# %(message)s用户输出的消息