import os
import sys

# 要单独跑这个类，需要放开注释
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from loguru import logger
from config import YamlConfig


class Logger:
    
    def __init__(self):

        config = YamlConfig()
        logger_config = config.__getattr__(name="logger")

        log_dir = logger_config["log_dir"]
        log_file = logger_config["file_name"]
        level = logger_config["level"]
        rotation_time = logger_config["rotation_time"]

        #日志目录如果不存在，创建日志目录并拼接日志文件路径
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file_path = os.path.join(log_dir,log_file)

        #移除默认的logger配置
        logger.remove()

        logger.add(sys.stdout, level=level)
        logger.add(log_file_path,rotation=rotation_time,level=level)
        self.logger = logger

LOG = Logger().logger

if __name__ == "__main__":

    LOG.debug("This is a debug message.")
    LOG.info("This is an info message.")
    LOG.warning("This is a warning message.")
    LOG.error("This is an error message.")