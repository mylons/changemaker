from unittest import TestCase
from change.util import ChangeMaker
from change.util import combinations


# test change maker
class ChangeMakerTests(TestCase):

    def setUp(self):
        # assumes no common use of 50 cent piece when calling it us
        self.us_coins = ChangeMaker([25, 10, 5, 1])
        self.us_no_penny = ChangeMaker([25, 10, 5])

    def test_change(self):
        self.assertEqual(self.us_no_penny.change(8), [])
        lists = self.us_coins.change(8)
        self.assertEqual(len(lists), 2)

        l1, l2 = lists
        self.assertEqual(sum(l1), 8)
        self.assertEqual(sum(l2), 8)
        self.assertEqual(l1.index(5) >= 0 or l2.index(5) >= 0, True)

    def test_combinations(self):
        result = combinations([1, 5, 10, 25], 8)
        self.assertEqual(len(result), 2)

