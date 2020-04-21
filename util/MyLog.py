import logging, os, time

class MyLog():
    def __init__(self):
        # 获取日志Logs目录，如果不存在，自动创建
        filepath = os.path.join(os.getcwd(), 'Logs')
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        # 创建日志文件，每天只会有一个文件，命名为当日时间.log
        filename = time.strftime('%Y-%m-%d', time.localtime())
        self.filename = os.path.join(filepath, filename+'.log')

    def log(self, level, message):
        '''
        步骤：1. 创建logger实例
             2. 设置logger日志级别权限
             3. 创建FileHandler，参数传入文件名(FileHandler默认使用GBK编码方式，需要修改为utf-8编码方式，修改FileHandler的__init__()方法
             4. 设置日志打印格式，并绑定到FileHandler
             5. 将handler绑定到logger上，并根据输入级别打印不同级别的日志
             6. 切记要解除handler的绑定，否则日志打印会重复
        '''
        logger = logging.getLogger()
        logger.setLevel(level=logging.DEBUG)
        th = logging.FileHandler(self.filename)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        th.setFormatter(formatter)
        logger.addHandler(th)
        if level == 'debug':
            logger.debug(message)
        elif level == 'info':
            logger.info(message)
        elif level == 'error':
            logger.error(message)
        elif level == 'warning':
            logger.warning(message)
        else:
            logger.critical(message)

        logger.removeHandler(th)


if __name__ == '__main__':
    # print(MyLog().filename)
    log = MyLog()
    log.log('debug', '我是debug')
    log.log('info', '我是info')
    log.log('error', '我是error')
    log.log('warning', '我是warning')