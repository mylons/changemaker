__author__ = 'mylons'


def combinations(values, total):
    """
    loosely modeled after the itertools combinations
    :param values: list of integers
    :param total: the sum the combination should sum to
    :return: list of lists of combinations: [[1, 2, 3], [4, 5, 6]]
    """
    def helper(list_of_values, total_sum):
        if total_sum <= 0:
            # base case is an empty list
            # (adding an empty list to a list does nothing in python)
            return []
        elif list_of_values:  # still more values to try
            value = list_of_values[-1]
            if value <= total_sum:
                number_of_cells = total_sum / value
                return ([value] * number_of_cells) + helper(list_of_values, total_sum - (value * number_of_cells))
            elif value > total_sum:  # another case where the value is too big
                # coin is too big, pop it off
                list_of_values.pop()
                return [] + helper(list_of_values, total_sum)
        else:
            return []

    results = []
    while values:
        result = helper(values[:], total)
        if result and sum(result) == total:
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
        # cache of amounts mapped to results
        self._cache = {}

    def change(self, amount):
        """
        returns a list of lists of possible ways to distribute
        the change
        :param amount: amount to make change
        :return: list of lists of ints
        """
        # for each combination
        return combinations(self._coins[:], amount)

    def count_change(self, amount):
        """
        returns the total # of ways to make change with this amount
        :param amount:
        :return:
        """
        # completely unoptimized
        return len(self.change(amount))


