from unittest import TestCase
from change.util import ChangeMaker


# test change maker
class ChangeMakerTests(TestCase):

    def setUp(self):
        # assumes no common use of 50 cent piece when calling it us
        self.us_coins = ChangeMaker([25, 10, 5, 1])
        self.us_no_penny = ChangeMaker([25, 10, 5])
        self.small = ChangeMaker([2, 1])

    def test_coins_are_sorted(self):
        # this might be frivolous, but _combinations relies on
        # a certain order
        self.assertListEqual(self.us_coins._coins, [1, 5, 10, 25])

    def test_change(self):
        self.assertEqual(self.us_no_penny.change(8), [])
        lists = self.us_coins.change(8)
        self.assertEqual(len(lists), 2)

        l1, l2 = lists
        self.assertEqual(sum(l1), 8)
        self.assertEqual(sum(l2), 8)
        self.assertEqual(l1.index(5) >= 0 or l2.index(5) >= 0, True)

    def test_count_change(self):
        self.assertEqual(self.us_coins.count_change(8), 2)
        self.assertEqual(self.us_no_penny.count_change(8), 0)

    def test_combinations(self):
        result = self.small._combinations([1, 5, 10, 25], 8)
        self.assertListEqual(sorted(result), [1, 1, 1, 5])

        result = self.small._combinations([1, 2], 3)
        self.assertListEqual(sorted(result), [1, 2])


