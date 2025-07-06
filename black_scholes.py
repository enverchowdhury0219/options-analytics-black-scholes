# functions that use the black-scholes framework to calculate price and delta of a european call option
import numpy as np
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type='call'):
    """
    this function returns the black-scholes price value for a european option.
    
    assumptions used are:
    -interest rate is known and constant throughout time
    -stock follows a random walk in continuous time, and the variance of the stock price 
    follows a log-normal distribution
    -volatility is constant
    -stocks pays no dividends
    -since this is a european option, can only be exercised at at expiration
    
    
    S: current stock price
    K: strike price
    T: time to expiration in years
    r: risk-free interest rate (e.g., 0.01 for 1%)
    sigma: volatility (e.g., 0.2 for 20%)
    option_type: 'call' or 'put' (call option in this case)
    """
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == "call":
        return  S * norm.cdf(d1) - K * np.exp(-r*T)* norm.cdf(d2)
    elif option_type == "put":
        return  K * np.exp(-r * T)*norm.cdf(-d2) - S*norm.cdf(-d1)
    else:
        raise ValueError("option_type variable must either be a call or a put")
    
def black_scholes_delta(S, K, T, r, sigma, option_type='call'):
    """
    this function returns the black scholes delta value for a european option, which is the rate of change of
    the option price with respect to the stock price. 
    
    assumptions used are:
    -interest rate is known and constant throughout time
    -stock follows a random walk in continuous time, and the variance of the stock price
    follows a log-normal distribution
    -volatility is constant
    -stocks pays no dividends
    -since this is a european option, can only be exercised at at expiration
    

    S: current stock price
    K: strike price
    T: time to expiration in years
    r: risk-free interest rate (e.g., 0.01 for 1%)
    sigma: volatility (e.g., 0.2 for 20%)
    option_type: 'call' or 'put' (call option in this case)
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    if option_type == "call":
        return norm.cdf(d1)
    elif option_type == "put":
        return -norm.cdf(-d1)
    else:
        raise ValueError("option_type variable must either be a call or a put")

