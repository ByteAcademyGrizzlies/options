class OptionLeg:

    def __init__(self, side, option_type, underly_price, contract_price):
        self.side = side
        self.option_type = option_type
        self.underly_price = underly_price
        self.contract_price = contract_price
        self.strategy = str(side + '_' + option_type).lower()
        
