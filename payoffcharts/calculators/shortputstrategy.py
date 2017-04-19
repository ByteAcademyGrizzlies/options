from .basestrategy import BaseStrategy


class ShortPutStrategy(BaseStrategy):
    """Strategy for selling a Put option"""

    STRATEGY_NAME = "Sell_Put"

    def __init__(self):
        super(ShortPutStrategy, self).__init__()

    def calculate_payoff(self, leg, stock_price):
        payoff = 0

        """If the underlying stock price is lower than the strike of the put
        the payoff is the difference between the price of the underlying
        and the strike"""
        if(stock_price < leg.strike):
            payoff += stock_price - leg.strike

        """Given that this is a sell, the price of the option gets added
        to the payoff"""
        payoff += leg.price

        return payoff
