# create a test to validate the methods from RemainderCheck class
import unittest
import pytest

from multicheck import MultiCheck


class Multi_test(unittest.TestCase):
    #create an object of the class RemainderCheck to test
    div = MultiCheck()
    # assertions to write our test cases
    def test_divisible(self):
        self.assertEqual(self.div.remainder(6, 3), 0)

    #assertions to validate the perrcentage method
    def test_percent(self):
        self.assertEqual(self.div.percentage(10, 5), 50)

    #assertions to validate positivity method
    def test_positive(self):
        self.assertEqual(self.div.positivity(5), True)



