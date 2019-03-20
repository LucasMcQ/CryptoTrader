from cb import CB


class TestBot:
    def __init__(self):
        print("testing...")
        self.cb = CB()
    def dayHigh(self, tick):  
        return self.cb.get_24hr_high(tick)
    def printHighs(self):
        print("BTC high = " + tester.dayHigh("BTC-USD"))
        print("ETH high = " + tester.dayHigh("ETH-USD"))
        print("ZRX high = " + tester.dayHigh("ZRX-USD"))
        print("LTC high = " + tester.dayHigh("LTC-USD"))
        print("XLM high = " + tester.dayHigh("XLM-USD"))
    def printCurrentPrice(self, tick):
        print(tick + " = " + self.cb.get_price(tick))
    def printBalance(self, tick):
        self.cb.get_balance(tick)


tester = TestBot()
#tester.printHighs()
#tester.printCurrentPrice("BTC-USD")
tester.printBalance("USD")


