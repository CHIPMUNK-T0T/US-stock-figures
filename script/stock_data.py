import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError

class StockData:
    """
        入力されたティッカーの株価情報を取り扱う。
    """

    def __init__(self, ticker):
        """
        ティッカーの設定、その他メンバ変数の宣言

        Parameters:
            ticker : string
                株価情報を取得する対象のティッカーシンボル。
        """
        self.ticker = ticker.upper()
        self.price_data = pd.DataFrame()
    
    def get_ticker(self):
        """
        クラスが保持するティッカー名を返す。

        Returns:
            _ : string
                ティッカー名
        """
        return self.ticker
 
    def request_stock_price(self, interval='day', frequency=5, period=10):
        """
        株価情報をリクエストする。

        Parameters:
            interval : string
                取得するデータの時間軸。デフォルトは日足。
                入力は以下の3つを受け入れ、その他の値が入力された際はエラーを返す。
                'day'(日足)
                'week'(週足)
                'month'(月足)
            frequency : int
                取得するデータの時間足。デフォルトは5分。
            period : int
                取得するデータの期間。単位はinterval。デフォルトでは10日

        Returns:
            _ : DataFrame
                対象となるティッカーの株価情報。
        """

        if interval.lower() == 'day':
            period_type = share.PERIOD_TYPE_DAY
            frequency_type = share.FREQUENCY_TYPE_MINUTE
        elif interval.lower() == 'week':
            period_type = share.PERIOD_TYPE_WEEK
            frequency_type = share.FREQUENCY_TYPE_DAY
        elif interval.lower() == 'month':
            period_type = share.PERIOD_TYPE_MONTH
            frequency_type = share.FREQUENCY_TYPE_MONTH

        stock = share.Share(self.ticker)

        try:
            stock_data = stock.get_historical(period_type=period_type, period=period, frequency_type=frequency_type, frequency=frequency)
        except YahooFinanceError as e:
            print(f'>>> [{self.get_ticker}] : {e.message}')
            return None
        
        print('{0}の株価情報を正常に取得しました。'.format(self.ticker))

        self.price_data = pd.DataFrame(data=stock_data)
        self.price_data['datetime'] = pd.to_datetime(self.price_data['timestamp'], unit="ms")
        self.price_data['datetime'] = self.price_data['datetime'] - datetime.timedelta(hours=5) # アメリカ東部時間
        self.price_data.set_index('datetime', inplace=True)
        self.price_data.drop(columns='timestamp', inplace=True)

    def get_stock_data(self):
        return self.price_data