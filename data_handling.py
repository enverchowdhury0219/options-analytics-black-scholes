import yfinance as yf
import pandas as pd

def get_spy_data(start='2015-01-01', end='2025-01-01'):
    """
    retrieves close prices of the SPY ETF within a given time interval (here being the last 10 years)
    
    example output:
    Price            Close
    Ticker             SPY
    Date                  
    2020-01-02  299.406403
    2020-01-03  297.139252
    2020-01-06  298.272858
    2020-01-07  297.434174
    2020-01-08  299.019318
    ...                ...
    2022-12-23  370.189178
    """
    spy = yf.download('SPY', start=start, end=end)
    spy = spy[['Close']]
    spy.dropna(inplace=True)
    return spy