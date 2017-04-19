import abc


class BaseStrategy(abc.ABC):
    """The base class for all options strategies"""

    STRATEGY_NAME = "Base"

    def __init__(self):
        super(BaseStrategy, self).__init__()
        pass

    @abc.abstractmethod
    def calculate_payoff(self, leg, stock_price):
        """The abstract method that MUST be implemented by any option strategy
        sub-class"""
        raise NotImplementedError
