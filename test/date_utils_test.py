import unittest

from common_utils import date_utils
from common_utils.print_method_name import PrintMethodName


class DateUtilsTest(unittest.TestCase):

    """
    compute_week_time
    """
    # @PrintMethodName()
    # def test_compute_week_time_default(self):
    #     real_start_time, real_end_time = date_utils.compute_week_time()
    #     expect_start_time = "2019-10-05"
    #     expect_end_time = "2019-10-11"
    #     self.assertEqual(expect_start_time, real_start_time)
    #     self.assertEqual(expect_end_time, real_end_time)

    @PrintMethodName()
    def test_compute_week_time_special_1(self):
        input_time = "2019-09-29"
        real_start_time, real_end_time = date_utils.compute_week_time(input_time=input_time)
        expect_start_time = "2019-09-28"
        expect_end_time = "2019-10-04"
        self.assertEqual(expect_start_time, real_start_time)
        self.assertEqual(expect_end_time, real_end_time)

    @PrintMethodName()
    def test_compute_week_time_special_2(self):
        input_time = "2019-09-25"
        real_start_time, real_end_time = date_utils.compute_week_time(input_time=input_time)
        expect_start_time = "2019-09-21"
        expect_end_time = "2019-09-27"
        self.assertEqual(expect_start_time, real_start_time)
        self.assertEqual(expect_end_time, real_end_time)

    """
    compute_last_week_time
    """
    # @PrintMethodName()
    # def test_compute_last_week_time_default(self):
    #     real_start_time, real_end_time = date_utils.compute_last_week_time()
    #     expect_start_time = "2019-09-28"
    #     expect_end_time = "2019-10-04"
    #     self.assertEqual(expect_start_time, real_start_time)
    #     self.assertEqual(expect_end_time, real_end_time)

    @PrintMethodName()
    def test_compute_last_week_time_special_1(self):
        input_time = "2019-09-29"
        real_start_time, real_end_time = date_utils.compute_last_week_time(input_time=input_time)
        expect_start_time = "2019-09-21"
        expect_end_time = "2019-09-27"
        self.assertEqual(expect_start_time, real_start_time)
        self.assertEqual(expect_end_time, real_end_time)

    @PrintMethodName()
    def test_compute_last_week_time_special_2(self):
        input_time = "2019-09-25"
        real_start_time, real_end_time = date_utils.compute_last_week_time(input_time=input_time)
        expect_start_time = "2019-09-14"
        expect_end_time = "2019-09-20"
        self.assertEqual(expect_start_time, real_start_time)
        self.assertEqual(expect_end_time, real_end_time)
