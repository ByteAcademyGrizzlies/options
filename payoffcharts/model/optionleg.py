class OptionLeg:
    '''An individual leg within an option strategy.
    This could be a trade either for an option or the underlying'''

    def __init__(self, side, type, strike, price):
        self.side = side
        self.type = type
        self.strike = strike
        self.price = price

        # Set the strategy that this leg represents
        self.strategy = self.side + '_' + self.type

    def get_strategy(self):
        return self.strategy

    def __str__(self):
        return "Option Leg: Side: {}, Type: {}, Strike: {}, Price: {}, \
            Strategy {}".format(self.side,
                                self.type,
                                self.strike,
                                self.price,
                                self.strategy)
