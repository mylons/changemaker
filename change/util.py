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
        self._coins = sorted(coins)

    def change(self, amount):
        """
        returns a list of lists of possible ways to distribute
        the change
        :param amount: amount to make change
        :return: list of lists of ints
        """
        # create the list from the generator
        return [c for c in self._combinations(amount)]

    def count_change(self, amount):
        """
        returns the total # of ways to make change with this amount
        runs in O(N*M) time.

        Similar to a power set, in the sense that it goes through
        all combinations and adds a coin to each one
        :param amount:
        :return:
        """
        # initialize set
        solutions = [1]
        solutions += [0] * (amount + 1)

        for coin in self._coins:
            # for all possible amounts from this coin to
            # the final amount
            for x in xrange(coin, amount + 1):
                # tally up the # of ways
                solutions[x] += solutions[x - coin]

        return solutions[amount]

    def _combinations(self, amount):
        """
        :param amount: to generate change combinations for
        :return: generator for list of lists of all combinations of change
        """
        def helper(coins, solution=[]):
            """
            helper function to ease the recursion and make the
            api to _combinations simpler
            :param coins: list of coins to combine
            :param solution: the eventual list containing the solution
            :return: generator to create the list of lists
            """
            # test this combination to see if we've found a
            # potential solution
            the_sum = sum(solution)
            if the_sum == amount:
                yield solution
            # no combination possible
            elif the_sum > amount or not coins:
                return
            # create every possible combination
            else:
                # this generator creates every combination for multiples of the same coin runs for every duplicate coin
                # it can until the sum is reached, exceeded, or there are no more coins.
                # worst case is O(M) where M is number of lists of repeated coins to achieve the sum.
                for coin_combo in helper(coins[:], (solution + [coins[0]])):
                    yield coin_combo
                # this generator is the iterator through the list, and as a result will cause a
                # O(N^2*M) solution
                for coin_combo in helper(coins[1:], solution):
                    yield coin_combo
        # start up the recursion
        return helper(self._coins)

