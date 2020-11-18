from lianxi.unit import GetExcel
import unittest
from parameterized import parameterized


class LoginTest(unittest.TestCase):
    aa = GetExcel().load(r"E:\ApiAutoTest\LeamPytest\pytest_cache\lianxi\data.xlsx","Sheet1")
    print(aa)

        






