# list of URLs

AUTHENTICATE='https://developers.tradeking.com/oauth/'

# Stock exchange abbreviations
EXCHANGE_ASE='A'
EXCHANGE_NYSE='N'
EXCHANGE_NASDAQ='Q'

BASE='https://api.tradeking.com/v1/'

# Account calls
ACCOUNTS_ALL=BASE+'accounts.xml'
BALANCES_ALL=BASE+'accounts/balances.xml'
ACCOUNT=BASE+'accounts/%s.xml'
ACCOUNT_BALANCE=BASE+'accounts/%s/balances.xml'
ACCOUNT_HISTORY=BASE+'accounts/%s/history.xml'
ACCOUNT_HOLDINGS=BASE+'accounts/%s/holdings.xml'

# Order/Trade calls

#Market Calls
MARKET_CLOCK=BASE+'market/clock.xml'
MARKET_QUOTES=BASE+'market/ext/quotes.xml?symbols=%s' # comma-delimited list of symbols
MARKET_NEWS_SEARCH=BASE+'market/news/search.xml?symbols=%s&maxhits=%d'
MARKET_NEWS_BY_ID='market/news/%s.xml' # id of article
MARKET_OPTIONS_SEARCH='market/options/search.xml?symbol=%s&query=%s' # this will need a specialized function
MARKET_OPTIONS_STRIKES='market/options/strikes.xml?symbol=%s' # symbol list
MARKET_OPTIONS_EXPIRATIONS='market/options/expirations.xml?symbol=%s' # symbol list
MARKET_TIMESALES='market/timesales.xml?symbols=%s&startdate=%s&interval=%s' #symbol list, YYYY-MM-DD, interval (i.e. 1m)
MARKET_TOPGAINERS_PCT=BASE+'market/toplists/toppctgainers.xml?exchange=%s'
MARKET_TOPGAINERS=BASE+'market/toplists/topgainers.xml?exchange=%s'
MARKET_TOPACTIVE=BASE+'market/toplists/topactive.xml?exchange=%s'
MARKET_TOPVOLUME=BASE+'market/toplists/topvolume.xml?exchange=%s'
MARKET_TOPLOSERS_PCT=BASE+'market/toplists/toppctlosers.xml?exchange=%s'
MARKET_TOPLOSERS=BASE+'market/toplists/toplosers.xml?exchange=%s'

MEMBER_PROFILE=BASE+'member/profile.xml'
