from sort import *
import unittest
from random import sample

class TestSorting(unittest.TestCase):
    def setUp(self):
        self.values_reversed = list(range(20000,-1, -1))
        self.values_random = sample(self.values_reversed, len(self.values_reversed))
        self.expected = list(range(20001))

    def test_merge(self):
        result1 = merge_sort(self.values_random)
        result2 = merge_sort(self.values_reversed)
        self.assertListEqual(result1, self.expected)
        self.assertListEqual(result2, self.expected)

    def test_insertion(self):
        result1 = merge_sort(self.values_random)
        result2 = merge_sort(self.values_reversed)
        self.assertListEqual(result1, self.expected)
        self.assertListEqual(result2, self.expected)
