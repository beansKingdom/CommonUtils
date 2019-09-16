import os
import logging
import datetime


class NewLog:

    def __init__(self, file_name):
        filename = os.path.basename(file_name)
        self.log = logging.getLogger(filename)
        self.log_file_path = self.build_path()

        # level = INFO
        logging.basicConfig(level="DEBUG",
                            format='%(asctime)s [%(filename)s line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a %d %b %Y %H:%M:%S',
                            filename=self.log_file_path,
                            filemode='a')

    def get_log(self):
        return self.log

    @staticmethod
    def build_path():
        temp_path = os.path.dirname(os.path.realpath(__file__))
        log_path = temp_path + "/../../static/log/"
        log_file_path = "%sdata_factory_%s.log" % (
            log_path, datetime.datetime.now().strftime("%y%m%d"))
        return log_file_path
