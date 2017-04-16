# Option Payoff Scenarios

### Objective
Students will need to implement a program that produces the payoff that will come about when investing in equity derivatives (Options). The program needs to take in the details of the options that an investor wants to invest in, and it needs to print out the range of the payoff (return) that the investor will receive as the underlying stock ranges from a price of $0 - $100.

eg. If the investor chooses to buy a Call option with a price of $5 and a strike of $50, the investor would see the following payoff as the stock price varies from $0 - $100.

{0: -5, 1: -5, 2: -5, 3: -5, 4: -5, 5: -5, 6: -5, 7: -5, 8: -5, 9: -5, 10: -5, 11: -5, 12: -5, 13: -5, 14: -5, 15: -5, 16: -5, 17: -5, 18: -5, 19: -5, 20: -5, 21: -5, 22: -5, 23: -5, 24: -5, 25: -5, 26: -5, 27: -5, 28: -5, 29: -5, 30: -5, 31: -5, 32: -5, 33: -5, 34: -5, 35: -5, 36: -5, 37: -5, 38: -5, 39: -5, 40: -5, 41: -5, 42: -5, 43: -5, 44: -5, 45: -5, 46: -5, 47: -5, 48: -5, 49: -5, 50: -5, 51: -4, 52: -3, 53: -2, 54: -1, 55: 0, 56: 1, 57: 2, 58: 3, 59: 4, 60: 5, 61: 6, 62: 7, 63: 8, 64: 9, 65: 10, 66: 11, 67: 12, 68: 13, 69: 14, 70: 15, 71: 16, 72: 17, 73: 18, 74: 19, 75: 20, 76: 21, 77: 22, 78: 23, 79: 24, 80: 25, 81: 26, 82: 27, 83: 28, 84: 29, 85: 30, 86: 31, 87: 32, 88: 33, 89: 34, 90: 35, 91: 36, 92: 37, 93: 38, 94: 39, 95: 40, 96: 41, 97: 42, 98: 43, 99: 44, 100: 45} 

The program should output a dict that has as its key the stock price, and the value representing the return that the investor would receive for that stock price key. The dict should 101 entires in total with the keys going from $0 - $100.

In order to implement a solution for this, you should proceed in the following steps.

#### User Investment Input (Option Leg)
Implement a class that represents a single leg of the user's option investment strategy. This will be a class that has attributes that represent the option type (Call or a Put), the investment action of the user (Buying or Selling) the Strike price of the option, and the price of the option. It should also implement a function called "get_strategy" which returns a string that holds the name of the simple investment strategy that this leg represents.
There should be one instance of this class for each leg of the users investment strategy. This class would represent the data of the application that will drive the solution

### Calculators
These classes should implement the calculation for a particular option investment strategy. There needs to be one class for each of the following simple option investment strategy

1. Buying a Call Option
2. Selling a Call Option
3. Buying a Put Option
4. Selling a Put Option

These classes should implement a function called "calculate_payoff" that takes 2 arguments: An instance of the Option Leg class the stock price. This function is where the algorithm for the simple investment strategy should be implemented. Remember the specifics of these that we discussed for General Options https://github.com/ByteAcademyCo/parttimefinance/tree/master/options#option-payoff-scenarios

### Payoff Calculator
Finally there needs to be a calculator class that ties the entire application together. This class should hold a registry of Option calculators. It's main job is to accept the user's investment input, figure out what Option calculator(s) the investment strategy maps to and calculate the overall payoff. 
Remember that the payoff is calculated by trying out what the value of the user's return would be as the stock price moves from a range of $0 to $100. So the calculate function in this class, should iterate through a range of 0 - 100 of possible stock price values and for each possible stock price, call the calculate function of the option calculators that match the user's investment strategy. If there are multiple option calculators involved in the users investment strategy, the calculate function must be called for each calculator and the values returned by all of the calculators should be summed up, as the overall return (payoff) that the user will receive for that stock price. This function should return a dictionary that has the stock price as its keys and the return for that stock price as the values.
