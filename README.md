
# Equity Derivatives: Options

### Objective
Students will be exposed to Equity Derivatives (Options) as a financial instrument and get an overview of the way they work and the various investment strategies that they are used for in the market place. They will be required to implement a python option payoff calculator that will calculate the return that an investor would receive for a set of option investment strategies.


## Options
Options are derivative instruments used in the market place by investors and speculators alike. They are derived from the underlying stock or commodity and as such do not exist without the stock (hence the name derivative). They are used in the following ways in the market place

 * Speculative investments: An investor would buy a Call option as a bet that the underlying stock would go up in the next 30 days
 * Risk Control (hedge): An oil company would buy a Put option on Oil (the underlying) to guarantee a sale at a fixed price
 * Income Generation: An investor that holds stock of a company and thinks it will go down in the short term would sell a Call Option as a bet that the stock will not go above a certain point

### Options represent a contract
An Option is a contract between two parties about the future price of the underlying. By buying an option, an investors acquires the *right* (not the obligation) to buy or sell the underlying at a particular price by a particular date in the future. The seller of the option has the *obligation* to trade the underlying to the buyer if the buyer does choose to exercise their right.

### Option Types
Basic options are of two types

1. Call 
 * Provides the owner the right to **Buy** the underlying at a fixed price on a given date in the future
 * Buying a call is a **bullish** bet on the underlying stock, in that it is a bet that the underlying stock will go up by the future date
1. Put
 * Provides the owner the right to **Sell** the underlying at a fixed price on a given date in the future
 * Buying a put is a **bearish** bet on the undering stock: the holder expects the underlying stock to trader lower at the future date

Depending on whether the investor has a bullish or bearish outlook on the underlying, they may choose to either buy or sell calls or puts

### Option Components
An option is made up of 3 parts

1. The type: Call or a Put
1. The Strike: The price at which the future trade is agreed upon
1. The Expiration date: The date in the future by which the owner of the option can be exercised

When two parties trade an option they are essentially getting into a contract to Buy or Sell the stock at a particular price (Strike) at a particular date (Expiration date).

### Option Variants
There are two main trade variants of Options

1. American Options: Can be exercised at any date between the purchase date and the expiration date
2. European Options: Can only be exercised on the expiration date

### Option Payoff Scenarios
Options are often analysed based on the payoff or return that they offer to traders. This is done by evaluating the size of the return that the trader would make (or lose) depending on different values of the underlying stock.

The basic strategies are the following. The best way to understand this is by viewing the payoff chart for the option strategies https://web2-nikhilpanchal.c9users.io/index.html#/charts

 * Buying a Call Option (a bet that the underlying stock would go up)
   * If the price of the underlying is above the strike price, your return is the difference between the underlying and the strike price net of the premium you paid to buy the option
 * Buying a Put Option (a bet that the underling stock would go down)
   * If the price of the underlying is below the strike price, your return is the difference between the strike price and the underlying net of the premium you paid to buy the option  
 * Selling a Call Option (a bet that the underlying stock would not go above a certain price)
   * The initial return is the premium you obtained from selling the Call. The return will stay at this level as long as the price of the underlying is below the strike price. Once the underlying moves above the strike price, your return will drop by the difference between the underlying and the strike price (The return can be --very-- negative as the underlying goes far enough above the strike)
 * Selling a Put Option (a bet that the underlying stock would not go below a certain price)
   * The initial return is the premium you obtained from selling the Put. The return will stay at this level as long as the price of the underlying is above the strike price. Once the underlying moves below the strike price, your return will drop by the difference between the strike price and the underlying (The return can be --very-- negative as the underlying goes far enough below the strike)

### How do Options work ? 

#### Calls
A trader buys a Call Option for NFLX (Netflix) with a strike price of $100, expiring on June 17th for a price of $9.20. This is a bet that between now and June 17th, the price of NFLX will go above $100. Given that NFLX as of now is trading at $94.76 the option is currently said to be *Out-of-the-money*. Between now and June 17th the following situations could occur resulting in different returns for the trader.

##### May 30th. NFLX moves to $120
 * The option is **In-the-money**
 * The premium on the option (price of the option) will potentially be higher than the initial purchase price
 * The holder could choose to sell the option or exercise it by buying NFLX at a 16% discount ((120 - 100) / 120)

##### May 30th. NFLX moves to $94
 * The option is **Out-of-the-money**
 * The premium on the option will be lower than the initial purchase price
 * The holder could choose to cut their losses and sell the option at a discount and take the loss, or they could choose to hold on to it hoping NFLX will swing back into the money. By doing the latter, the holder runs the risk of losing all the money the spent in buying the option if it expires worthless
 
##### Expiration date: June 17th
Two scenarios could arise here.

###### NFLX is above $100
 * The option expires in the money, allowing the holder to exercise it and buy NFLX at $100. They could choose to either immediately sell it in the market and pocket the difference or hold on to NFLX by buying it at a discount.  

###### NFLX is below $100
 * The option expires worthless. The trader has lost all the money they paid to buy this option. tough luck son :(

#### Puts
A trader buys a Put Option for GOOG (Alphabet Inc) with a strike price of $700, expiring on June 17th for a price of $42.80. This is a bet that between now and June 17th, the price of GOOG will go below $700. Given that GOOG as of now is trading at $$708 the option is currently said to be *Out-of-the-money*. Between now and June 17th the following situations could occur resulting in different returns for the trader.

##### May 30th. NFLX moves to $750
 * The option is **Out-of-the-money**
 * The premium on the option will be lower than the initial purchase price
 * The holder could choose to cut their losses and sell the option at a discount and take the loss, or they could choose to hold on to it hoping GOOG will swing back into the money. By doing the latter, the holder runs the risk of losing all the money the spent in buying the option if it expires worthless

##### May 30th. NFLX moves to $650
 * The option is **In-the-money**
 * The premium on the option (price of the option) will potentially be higher than the initial purchase price
 * The holder could choose to sell the option or exercise it by selling GOOG at a 7.5% premium ((700 - 650) / 650)

##### Expiration date: June 17th
Two scenarios could arise here.

###### GOOG is above $700
 * The option expires worthless. The trader has lost all the money they paid to buy the Put option. 

###### GOOG is below $700
 * The option expires in the money, allowing the holder to exercise it and sell GOOG at $700. The trader would buy GOOG in the open market at the price < $700 and pocket the difference by selling it at $700.  
 
Essentially, with option trades you can
1. Exercise the Options: And your return will be the difference between the underlying and the strike price
1. Options Expire worthless: You lose all the money you paid (premium) to buy the option
1. Sell the Option: Your return will be the difference between the sale and purchase price of the option

Trading with options is regarded High Risk / High Reward. You could either make a return worth multiples of the amount you invested to buy options (If the options float from out to in the money), or you could just as easily lose 100% of the money invested (if the options are out of the money at expiration and expire worthless).


### Option Pricing
There are fairly complex financial models used to price an option, the most common one used is the Black-Sholes model, that takes into account the following components of the option.

1. The type: Call or Put
1. The Strike Price: The farther away the strike price is from the current price of the underlying the more exterme the pricing is
  * If the option is in the money, the further away the strike is the higher the price of the option (premium)
  * If the option is out of the money, the further away the strike is the lower the premium on the option
2. The Expiration Date: The farther the expiration date is, the higher the chance that the option has to eventually swing in to the money. Therefore the higher the premium on the option
3. The volatility of the underlying stock: The greater the volatility of the underlying stock, the higher the premium on the option. Volatile stocks undergo much larger price changes offering a greater potential for a positive return, hence they are higher priced.

### Option Trades

#### Speculative
eg. An investor who expects AAPL to trade above $100 by June, could possibly do the following
 * Buy a Call Option (a bet that AAPL will go up)
 * With a Strike of $100 (a bet that AAPL will go above $100)
 * With an Expiration date of June 18th (a bet that APPL will go above $100 by June 18th)

If AAPL does reach say $105 by June 18th, the owner of this call option would go ahead and exercise their *right to buy* AAPL at $100, and then subsequently sell it for $105 in the open market pocketing the $5 difference.

eg. A trader who expects TWTR to trade below $15 by June, could do the following
 * Buy a Put Option (a bet that TWTR will go down)
 * With a Strike of $15 (a bet that TWTR will do down below $15)
 * With an expiration date of June 18th (a bet that TWTR will go down below $15 by June 18th)

If TWTR does go below $15 by June 18th, the owner of the put option would exercise their *right to sell* TWTR at $15. They way they would make money is, assuming on June 18th TWTR is trading at $10, the trader would buy TWTR for $10.

Note that as the option goes deeper and deeper into the money, its own intrinsic value would rise accordingly. So instead of exercising the option, a trader could also choose to just sell the option and difference between the sale and purchase price of the option itself (*This is the most common way that options are traded*).

#### Risk Control (Hedging)
Options are often used to hedge the risk related to the underlying instrument. This is typically done by producers or consumers of commodities to lock the price in the future at which the commodity can be traded.

eg. An Oil company would Buy a Put option on the price of Oil at $70 on June 18th. 

This give the company the right to sell Oil at a minimum of $70 regardless of the price of Oil on June 18th.
Note that safer the bet the trader wants to make with the option the more expensive it gets. Given the price of Oil today, purchasing a Put Option for a strike price of $70 would be very expensive indeed.

Reference: http://www.bloomberg.com/news/articles/2016-02-09/oil-drillers-exposed-in-three-way-hedges-as-crude-dips-below-30

```
The trade has three parts. First, one option capped the best price Callon could get at $65 a barrel (Short Call).
Selling the right to profit if prices rise offsets the cost of protecting against a decline. The second piece established 
a floor price of $55, a guaranteed minimum that Callon would get paid even if oil fell below that point (Long Put).
By itself, this kind of trade, called a collar, would’ve ensured that Callon received $25 a barrel protection when oil is trading at $30.

However, Callon added a third element by selling a put option, sometimes called a subfloor, at $40 a barrel (Short Put). 
Below that point, Callon essentially forfeits part of its protection. Instead of pocketing $55, the company is only entitled
to the difference between the floor and that subfloor, or $15 a barrel in this case. At $30, Callon will realize $45 a barrel,
$10 a barrel less than it would’ve received with a traditional collar.
```

eg. An airline company would Buy a Call Option on the price of Oil at $30 by June 18th
This would allow the airline to lock in the trade at a price level of $30, essentially guarding against Oil going up by June

#### Income Generation
Option can often be used to generate Income. This is definitely risky, but is done nonetheless

eg. An investor looking at TSLA (Tesla Motors) may sell June 18th Call options with a strike price of $200. 

This is bet that TSLA would not go above $200 by June 18th, i.e. expecting that the Put Option would expire as worthless on June 18th  allowing the seller of this Put option to pocket the price at which it was sold. 
There is an element of risk here, because if the investor is wrong and TSLA does climb above $200, say to $210, the counter party would exercise their option to Buy the stock, which will force the investor to Buy TSLA on the Open market at $210 and sell it to the counter party at $200 thereby incurring a loss of $10. To reduce the risk the investor may consider first buying TSLA at where it is now, or write Put options on TSLA stock that he already might own.
Such a trade is known as a *Covered Call*

eg. A trader could sell the June 18th TSLA Put Option with a Strike of $160

This is a bet that TSLA will not go below $160 by June 18th, which if it does happen would allow the trader to pocket the money obtained from selling this option. 

### Option Jargon

 * Strike
 * In the Money
 * Out of the Money
 * Premium


### Trading Strategies

We've talked about the basic strategies to Buy and Sell Calls and Puts. However Options are often combined in multiple different ways to construct complex trades that cater to various scenarios and risk apettites of traders. Some common ones that we will look at are 

 * Straddle
 * Reverse Straddle
 * Covered Call
 * Strangle
 * Reverse Strangle
 * Clipped Reverse Strangle




