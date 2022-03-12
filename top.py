# coding: utf-8
from finvizfinance.quote import finvizfinance

class StateFull(object):  # Mutable oppozite to immutable
    def __init__(self):
        self.state_ = 0

    def increnet(self):
        self.state_ += 1

    def state(self):
        return self.state_

class Immutable(object):
    def __init__(self):
        self.state_ = 0

    #def increnet(self):
    #    self.state_ += 1

    def state(self):
        return self.state_

def StateLessPlus(a, b):
    return a+b

################################################################
################################################################
################################################################

class RuleValue(object):
    def __init__(self):
        self.filter_ = "P/E to Debt/Eq"

class RuleGrowth(object):
    def __init__(self):
        self.filter_ = "RoE to Gross Margin"

if __name__ == '__main__':

    avaible_sectors = ['Basic Materials']

    rules = [RuleValue(), RuleGrowth()]

    artifacts = "artifacts"

    for sector in avaible_sectors:
        for rule in rules:
            # Do request
            pass

    # Clean all
    #remove artifacts
    #mkdir artifacs ..

    # List
    tickers = ['tsla', 'amt']  # list

    # one to many
    ticker_to_stock = {}  # hash table

    for ticker in tickers:
        # Do againt
        stock = finvizfinance(ticker)
        ticker_to_stock[ticker] = stock

    for ticker in ticker_to_stock:
        ticker_to_stock[ticker].ticker_charts()

    state_full = StateFull()
    state_full.increnet() # Mutation
    state_full.increnet()
    # Was crated with 0, now ...?