from requests import get

class TradingOperations:
    
    def __init__(self) -> None:
        self.key = "a0633e553800497" # should be an env variable
        self.secret = "remyx2ubunntl3n"
        self.url = "https://api.tradingeconomics.com/country/mexico/?client={KEY}:{SECRET}".format(KEY=self.key , SECRET=self.secret)
        self.url_gdp = "https://api.tradingeconomics.com/country/{country}?c=guest:guest&group={group}"

    def get_info(self):
        return get(self.url)