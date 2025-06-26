from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, EURUSD

#testing a simple moving average strategy using the EURO to USD currency pair data
class MySMAStrategy(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 100)
        self.ma2 = self.I(SMA, price, 200)
        
    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()



backtest = Backtest(EURUSD, MySMAStrategy,  commission=.002, exclusive_orders = True)
stats = backtest.run()



backtest.plot()