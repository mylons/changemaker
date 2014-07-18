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
                return [value] + helper(list_of_values, total_sum - value)
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
            print "result = ", result
            print "result max is: ", max(result)
            values.remove(max(result))
            results.append(result)
        else:
            """
            nothing more to be done here
            optimizes the function slightly
            by not performing unecessary traversals through
            the values list
            """
            print "results = ", results
            return results


class ChangeMaker:

    def __init__(self, coins):
        assert isinstance(coins, list) and len(coins) > 0
        # sort coins into ascending order so we can
        # use a list as a stack and just self._coins.pop()
        # to get the next largest value
        coins.sort()
        self._coins = coins

    def change(self, amount):
        # for each combination
        return combinations(self._coins[:], amount)

    def count_change(self, amount):
        # completely unoptimized
        return len(self.count_change(amoutn))


