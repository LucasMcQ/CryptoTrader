from coinbase.wallet.client import Client
from cb_auth import CoinbaseExchangeAuth
import requests
import configparser
import json

class CB:
    def __init__(self, tick='BTC-USD'):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.api_url = config['coinbasepro']['APIURL']
        self.api_key = config['coinbasepro']['APIKey']
        self.secret_key = config['coinbasepro']['SecretKey']
        self.password = config['coinbasepro']['Password']
        self.auth = CoinbaseExchangeAuth(self.api_key.encode('utf8'), self.secret_key.encode('utf8'), self.password.encode('utf8'))
        self.balanceDict = self.constructDict()

    def constructDict(self):
        r = requests.get(self.api_url + 'accounts', auth=self.auth)
        currencyDict = {}
        elms = r.json()
        for key in elms:
            currencyDict[key['currency']] = key['id']
        
        return currencyDict

    def get_price(self, tick):
        r = requests.get('https://api.pro.coinbase.com/products/' + tick + '/ticker')
        return r.json()['price']

    def get_24hr_high(self, tick):
        r = requests.get('https://api.pro.coinbase.com/products/' + tick + '/stats')
        return r.json()['high']

    def get_24hr_low(self, tick):
        r = requests.get('https://api.pro.coinbase.com/products/' + tick + '/stats')
        return r.json()['low']
    
    def get_balance(self, tick):
        r = requests.get(self.api_url + 'accounts/' + self.balanceDict[tick], auth=self.auth)
        balance = r.json()#['balance']
        print(balance)
        return balance

    def test(self):
        # Get accounts
        r = requests.get(self.api_url + 'accounts', auth=self.auth)
        print(r.json())
