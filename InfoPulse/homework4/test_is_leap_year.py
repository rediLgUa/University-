import unittest
from homework3.solution6_yearsFunc import is_year_leap

class TestsLeapYear(unittest.TestCase):

    def test_positive_2000(self):
        res = is_year_leap(2000)
        self.assertEqual(res,True)
        self.assertTrue(res)

    def test_negative_2(self):
        res = is_year_leap(200)
        self.assertEqual(res,False)
        self.assertFalse(res,msg="ALL OK")