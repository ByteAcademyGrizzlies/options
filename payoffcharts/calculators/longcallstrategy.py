from .basestrategy import BaseStrategy


class LongCallStrategy(BaseStrategy):
    '''The strategy where you buy a Call Option'''

    STRATEGY_NAME = "Buy_Call"

    def __init__(self):
        pass

    def calculate_payoff(self, leg, stock_price):
        payoff = 0

        '''If the underlying stock price is above the strike price of the
        call option, the payoff is the difference between stock price and
        strike'''
        if(stock_price > leg.strike):
            payoff = stock_price - leg.strike

        '''Subtract the price of the call option'''
        payoff -= leg.price

        return payoff
