from .basestrategy import BaseStrategy


class LongPutStrategy(BaseStrategy):
    """The strategy for buying a put option"""

    STRATEGY_NAME = "Buy_Put"

    def __init__(self):
        super(LongPutStrategy, self).__init__()

    def calculate_payoff(self, leg, stock_price):
        payoff = 0

        """The payoff is the difference between the strike price and the
        price of the underlying stock"""
        if(stock_price < leg.strike):
            payoff += leg.strike - stock_price

        """Since this is a buy, the price gets subtracted from the payoff"""
        payoff -= leg.price

        return payoff
