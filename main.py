from black_scholes import black_scholes_delta
from data_handling import get_spy_data
import matplotlib.pyplot as plt

# Constants
T = 30 / 365    # Time to expiry in years (30 days)
r = 0.01        # Risk-free rate
sigma = 0.2     # Volatility

# Get SPY close prices
df = get_spy_data()
df['Close'] = df['Close'].astype(float)
df = df.reset_index(drop=False)  # Make date a column instead of index
df['DaysToExpiry'] = df.index.map(lambda i: 30 - (i % 30))
df['T'] = df['DaysToExpiry'] / 365
df['T'] = df['T'].astype(float)

df['Delta'] = df.apply(lambda row: black_scholes_delta(
    S=float(row['Close']),
    K=float(row['Close']),         # ATM
    T=float(row['T']),
    r=0.01,
    sigma=0.2
), axis=1)

#Plot delta over time
plt.figure(figsize=(12, 5))
plt.plot(df['Delta'])
plt.ylim(0.5, 0.52)
plt.title('SPY Call Option Delta Over Time')
plt.ylabel('Delta')
plt.xlabel('Date')
plt.grid(True)
plt.show()
