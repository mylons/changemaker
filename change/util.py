__author__ = 'mylons'


class ChangeMaker:

    def __init__(self, coins):
        """
        requires a list of integers as input
        :param coins: list of integers
        :return: ChangeMaker object
        """
        assert isinstance(coins, list) and len(coins) > 0
        # sort coins into ascending order so we can
        # use a list as a stack and just self._coins.pop()
        # to get the next largest value
        coins.sort()
        self._coins = coins

    def change(self, amount):
        """
        returns a list of lists of possible ways to distribute
        the change
        :param amount: amount to make change
        :return: list of lists of ints
        """
        # for each combination
        #return combinations(self._coins[:], amount)
        values = self._coins[:]  # copy the coins, this is deleterious
        results = []
        while values:
            result = self._combinations(values[:], amount)
            if result and sum(result) == amount:
                # remove the biggest to attempt another combination
                values.remove(max(result))
                results.append(result)
            else:
                """
                nothing more to be done here
                optimizes the function slightly
                by not performing unecessary traversals through
                the values list
                """
                return results
        # exhausted values, and helper consistently returned results
        return results

    def count_change(self, amount):
        """
        returns the total # of ways to make change with this amount
        :param amount:
        :return:
        """
        # completely unoptimized
        return len(self.change(amount))

    def _combinations(self, values, total):
        """
        finds combinations of coins that sum to total
        :param values: list of integers
        :param total: the sum the combination should sum to
        :return: list of lists of combinations: [[1, 2, 3], [4, 5, 6]]
        """
        if total <= 0:
            # base case is an empty list
            # (adding an empty list to a list does nothing in python)
            return []
        elif values:  # still more coins to try
            value = values[-1]
            if value <= total:
                number_of_cells = total / value
                return ([value] * number_of_cells) + self._combinations(values, total - (value * number_of_cells))
            elif value > total:  # another case where the coin is too big
                # coin is too big, pop it off
                values.pop()
                return [] + self._combinations(values, total)
        else:  # the other base case, no more coins
            return []

