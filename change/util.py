__author__ = 'mylons'


class ChangeMaker:

    def __init__(self, coins):
        assert isinstance(coins, list) and len(coins) > 0

        self._coins = coins
