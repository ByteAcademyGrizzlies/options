import matplotlib.pyplot as plt


class PayoffPlotter(object):
    """Class to Plot the option payoff scenarios"""

    def __init__(self):
        super(PayoffPlotter, self).__init__()

    def plot_payoff(self, payoff):
        """Accepts a dictionary with the keys as the underlying price
        and the values as the return for that price"""

        x_axis = list(payoff.keys())
        y_axis = list(payoff.values())

        plt.xlabel("Stock Price $")
        plt.ylabel("Return $")
        plt.title("Option Strategy Payoff")
        plt.grid(True)
        plt.axis([0, 12, -10, 12])
        plt.plot(x_axis, y_axis, label="Payoff")

        # Display the graph
        plt.show()
