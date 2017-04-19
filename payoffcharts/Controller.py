from calculators.longputstrategy import LongPutStrategy
from calculators.longcallstrategy import LongCallStrategy
from calculators.shortcallstrategy import ShortCallStrategy
from calculators.shortputstrategy import ShortPutStrategy
from calculators.longunderlying import LongUnderlying
from model.optionleg import OptionLeg
from payoffcalculator import PayOffCalculator
from view.graphview import PayoffPlotter


class Controller(object):
    """The Option Payoff Controller"""

    def __init__(self):
        super(Controller, self).__init__()

        self.calculator = PayOffCalculator()
        self.plotter = PayoffPlotter()

        # Register the strategies
        strategies = [LongPutStrategy(),
                      LongCallStrategy(),
                      ShortPutStrategy(),
                      ShortCallStrategy(),
                      LongUnderlying()]

        for strat in strategies:
            self.calculator.register_strategy(strat)

    def get_strategy_payoff(self, legs):
        payoff = self.calculator.calculate(legs)
        self.plotter.plot_payoff(payoff)


if __name__ == '__main__':
    controller = Controller()
    controller.get_strategy_payoff([OptionLeg("Buy", "Call", 9, 0),
                                    OptionLeg("Sell", "Call", 4, 0)])

#    controller.get_strategy_payoff([OptionLeg("Sell", "Call", 60, 20),
 #                                   OptionLeg("Sell", "Put", 40, 20),
  #                                  OptionLeg("Buy", "Put", 20, 10),
   #                                 OptionLeg("Buy", "Call", 80, 10)])


#
