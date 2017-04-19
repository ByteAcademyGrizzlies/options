from .basestrategy import BaseStrategy


class ShortCallStrategy(BaseStrategy):
    """Strategy for selling a call option"""

    STRATEGY_NAME = "Sell_Call"

    def __init__(self):
        super(ShortCallStrategy, self).__init__()

    def calculate_payoff(self, leg, stock_price):
        payoff = 0

        """If the underlying stock is lower than the strike
        Then the payoff is the difference between the underlying
        and the strike.
        For shorting a call, the payoff in this scenario is a
        negative value"""
        if(stock_price > leg.strike):
            payoff = leg.strike - stock_price

        """The price is added to the payoff because this is a sale of
        the option"""
        payoff += leg.price

        return payoff
