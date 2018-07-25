# primary api file for PyAlly
# contains authentication function as well as ally rest endpoint wrappers

import os
from requests_oauthlib import OAuth1Session


import constants

KEYSTORE=os.path.expanduser('~/.PYALLY_KEYS')

oathHandler = None


def initPyAlly():
    global oauthHandler
    keys = open(KEYSTORE, 'r').readlines()
    consumerKey = keys[0].split(' ')[1].strip()
    consumerSecret = keys[1].split(' ')[1].strip()
    authKey = keys[2].split(' ')[1].strip()
    authSecret = keys[3].split(' ')[1].strip()
    
    oauthHandler = OAuth1Session(consumerKey, client_secret=consumerSecret, resource_owner_key=authKey, resource_owner_secret=authSecret)

# Run an HTTP GET against the given endpoint, authenticated via the initialized oauthHandler
# Return: HTTP response
def genericGet(endPoint):
    if not oauthHandler:
        raise Exception('must call initPyAlly to initialize APIs!')
    return oauthHandler.get(endPoint)

##################################################################################
# ACCOUNT CALLS
# Run an HTTP GET against the Ally accounts endpoint
# Return: the resultant XML file
def getAllAccounts():
    return genericGet(constants.ACCOUNTS_ALL)

def getAllBalances():
    return genericGet(constants.BALANCES_ALL)

def getAccount(id):
    return genericGet(constants.ACCOUNT % id)

def getAccountBalance(id):
    return genericGet(constants.ACCOUNT_BALANCE % id)

def getAccountHistory(id):
    return genericGet(constants.ACCOUNT_HISTORY % id)

def getAccountHoldings(id):
    return genericGet(constants.ACCOUNT_HOLDINGS % id)


##################################################################################
# ORDER/TRADE CALLS

##################################################################################
# MARKET CALLS
def getMarketClock():
    return genericGet(constants.MARKET_CLOCK)

# IMPORTANT NOTE: if a ticker cannot be found, an error is not returned from the server
# instead, a quote is returned with the following symbol tag: <symbol>SYMBOL</symbol>
def getMarketQuotes(symbols):
    return genericGet(constants.MARKET_QUOTES % symbols)

def getTopGainersPct():
    return genericGet(constants.MARKET_TOPGAINERS_PCT % constants.EXCHANGE_NYSE)

def getTopLosersPct():
    return genericGet(constants.MARKET_TOPLOSERS_PCT % constants.EXCHANGE_NYSE)

##################################################################################
# MEMBER CALLS
def getMemberProfile():
    return genericGet(constants.MEMBER_PROFILE)

# TODO test function for calling wrapper functions
def testMarketQuotes():
    print getMarketQuotes('AAPL')
    print getMarketQuotes('AAPL,TSLA,O')
    print getMarketQuotes('AAPL,TSLA,O,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    print 'Finished testing market quotes...'

if __name__ == '__main__':
    initPyAlly()
    acctnum = 'xxxxxxxx'
    
    # account tests
    print getAllAccounts()
    print getAllBalances()
    print getAccount(acctnum)
    print getAccountBalance(acctnum)
    print getAccountHistory(acctnum)
    print getAccountHoldings(acctnum)

    # order/trade tests
    
    # market tests
    print getMarketClock()
    testMarketQuotes()
    print getTopGainersPct()
    print getTopLosersPct()
    
    # member tests
    print getMemberProfile()









