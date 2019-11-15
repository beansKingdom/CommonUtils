import unittest

from common_utils import date_utils
from common_utils.print_method_name import PrintMethodName


class DateUtilsTest(unittest.TestCase):

    """
    compute_week_time
    """
    # 分界点为本周五, 日期在本周五之前的周一计算时间Case
    @PrintMethodName()
    def test_compute_week_time_special_1(self):
        input_time = "2019-09-30"
        real_start_time, real_end_time = date_utils.compute_week_time(input_time=input_time)
        expect_start_time = "2019-09-28"
        expect_end_time = "2019-10-04"
        self.assertEqual(expect_start_time, real_start_time)
        self.assertEqual(expect_end_time, real_end_time)

    # 分界点为本周五, 日期在本周五之前的周三计算时间Case
    @PrintMethodName()
    def test_compute_week_time_special_2(self):
        input_time = "2019-09-25"
        real_start_time, real_end_time = date_utils.compute_week_time(input_time=input_time)
        expect_start_time = "2019-09-21"
        expect_end_time = "2019-09-27"
        self.assertEqual(expect_start_time, real_start_time)
        self.assertEqual(expect_end_time, real_end_time)

    # 分界点为本周五, 日期在本周五之后的周日计算时间Case
    @PrintMethodName()
    def test_compute_week_time_special_3(self):
        input_time = "2019-10-13"
        real_start_time, real_end_time = date_utils.compute_week_time(input_time=input_time)
        expect_start_time = "2019-10-05"
        expect_end_time = "2019-10-11"
        self.assertEqual(expect_start_time, real_start_time)
        self.assertEqual(expect_end_time, real_end_time)

    # 分界点为本周五, 日期在本周五当天的计算时间Case
    @PrintMethodName()
    def test_compute_week_time_special_4(self):
        input_time = "2019-10-11"
        real_start_time, real_end_time = date_utils.compute_week_time(input_time=input_time)
        expect_start_time = "2019-10-05"
        expect_end_time = "2019-10-11"
        self.assertEqual(expect_start_time, real_start_time)
        self.assertEqual(expect_end_time, real_end_time)

    """
    compute_last_week_time
    """
    # 分界点为周一, 计算当天时间为周日的上周时间Case
    @PrintMethodName()
    def test_compute_last_week_time_special_1(self):
        input_time = "2019-09-29"
        real_start_time, real_end_time = date_utils.compute_last_week_time(input_time=input_time)
        expect_start_time = "2019-09-14"
        expect_end_time = "2019-09-20"
        self.assertEqual(expect_start_time, real_start_time)
        self.assertEqual(expect_end_time, real_end_time)

    # 分界点为周一, 计算当天时间为周一的上周时间Case
    @PrintMethodName()
    def test_compute_last_week_time_special_2(self):
        input_time = "2019-09-23"
        real_start_time, real_end_time = date_utils.compute_last_week_time(input_time=input_time)
        expect_start_time = "2019-09-14"
        expect_end_time = "2019-09-20"
        self.assertEqual(expect_start_time, real_start_time)
        self.assertEqual(expect_end_time, real_end_time)

    """
    compute_time
    """
    def test_compute_time_default(self):
        real_time = date_utils.compute_time()
        expect_time = "2019-10-13"
        self.assertEqual(expect_time, real_time)

    # 计算前一天时间
    @PrintMethodName()
    def test_compute_time_special_1(self):
        real_time = date_utils.compute_time(-1)
        expect_time = "2019-10-12"
        self.assertEqual(expect_time, real_time)

    # 计算后一天时间
    @PrintMethodName()
    def test_compute_time_special_2(self):
        real_time = date_utils.compute_time(1)
        expect_time = "2019-10-14"
        self.assertEqual(expect_time, real_time)

    """
    compute_interval_time
    """
    def test_compute_interval_time_str(self):
        start_time = "2019-11-14"
        end_time = "2019-11-15"
        interval_time = date_utils.compute_interval_time(start_time, end_time)
        self.assertEqual(86400.0, interval_time)

    def test_compute_interval_time_str_1(self):
        start_time = "2019-11-14 14:15:00"
        end_time = "2019-11-14 15:00:00"
        format_time = "%Y-%m-%d %H:%M:%S"
        interval_time = date_utils.compute_interval_time(start_time, end_time, time_format=format_time)
        print(interval_time)
        self.assertEqual(2700.0, interval_time)
