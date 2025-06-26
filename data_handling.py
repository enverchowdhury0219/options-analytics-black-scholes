import yfinance as yf
import pandas as pd

def get_spy_data(start='2020-01-01', end='2024-01-01'):
    """
    this retrieves close prices of the SPY ETF within a given time interval
    
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
    2022-12-27  368.729309
    2022-12-28  364.146881
    2022-12-29  370.701630
    2022-12-30  369.725189
    """
    spy = yf.download('SPY', start=start, end=end)
    spy = spy[['Close']]
    spy.dropna(inplace=True)
    return spy