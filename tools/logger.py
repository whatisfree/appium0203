
import logging.handlers
import time

from item_path import DIR_NAME


class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cur_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            file_name = DIR_NAME + '/logs/' + cur_date + '.log'
            # 获取日志器(日记本)
            cls.logger = logging.getLogger()
            # 给日志器设置总的级别,级别是封装在logging里面的
            # 我要设置错误级别,完全大写
            cls.logger.setLevel(logging.INFO)
            # 2.获取格式器
            # 2.1这个只是要输出的样式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            # 2.2 获取格式器 参数  具体要输出什么样的样式
            fm = logging.Formatter(fmt)
            # 3.获取处理器  按时间切割的文件处理器工作中用midnight  ,backupCount=3  除了原件，只保存最新的三个
            tf = logging.handlers.TimedRotatingFileHandler(filename=file_name,
                                                      when='H',
                                                      interval=1,
                                                      backupCount=3,
                                                      encoding='utf-8')

            # 在处理器中添加格式器
            tf.setFormatter(fm)
            # 在日志器中添加处理器
            cls.logger.addHandler(tf)
        return cls.logger


if __name__ == '__main__':
    # 测试日志调用的时候
    logger = GetLogger().get_logger()
    logger.debug('调试')
    logger.info('信息')
    logger.warning('警告')
    logger.error('错误')
    logger.critical('致命的')