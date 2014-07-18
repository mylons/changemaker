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

"""
>>> cm = ChangeMaker([25, 10, 5, 1])
In ChangeMaker, write two functions called change() and count_change(), each of which takes as an argument the amount to be changed. The first function, change(), returns the combinations of the coins that can be used to sum up to the amount:

>>> cm.change(8)
[[5, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]
With the coin denominations 25, 10, 5, and 1, the amount 8 can be made up of one 5 and three 1's, or eight 1's. There are only two ways to make up an amount of 8 with those denominations. Order does not matter in the results, so [5, 1, 1, 1] and [1, 5, 1, 1] are not two different combinations.

If the amount given can not be made using the denominations, return an empty list []:

>>> cm = ChangeMaker([25, 10, 5])
>>> cm.change(8)
[]
The second function, count_change(), returns only the number of such combinations:

>>> cm = ChangeMaker([25, 10, 5, 1])
>>> cm.count_change(8)
2
>>> cm = ChangeMaker([25, 10, 5])
>>> cm.count_change(8)
0
The solution should be generalized to work with any denominations of coins (i.e., not typical currency denominations):

>>> cm = ChangeMaker([2, 1])
>>> cm.change(3)
[[2, 1], [1, 1, 1]]
>>> cm.count_change(3)
2
>>> cm.change(4)
[[2, 2], [2, 1, 1], [1, 1, 1, 1]]
>>> cm.count_change(4)
3
"""