import alpaca_trade_api as alpaca

class Connection_Handler:

    def __init__(self):
        self.api_key = None # Call DB and decrypt here
        self.secret = None # Call DB and decrypt here
        self.api_connection = alpaca.REST(self.api_key, self.secret, api_version ='v2')