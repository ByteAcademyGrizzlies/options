from .basestrategy import BaseStrategy


class LongUnderlying(BaseStrategy):
    """Strategy for buying the underlying stock"""

    STRATEGY_NAME = "Buy_Stock"

    def __init__(self):
        super(LongUnderlying, self).__init__()

    def calculate_payoff(self, leg, stock_price):
        payoff = 0

        payoff += stock_price - leg.price

        return payoff
