from black_scholes import black_scholes_delta, black_scholes_price
from data_handling import get_spy_data
import matplotlib.pyplot as plt

# constants we use
T = 30 / 365    # simulating one month expiry
r = 0.01        # risk-free rate
sigma = 0.2     # volatility

# getting the SPY close prices with yahoo finance
df = get_spy_data()
df['Close'] = df['Close'].astype(float)
df = df.reset_index(drop=False)  # make date a column instead of index
df['DaysToExpiry'] = df.index.map(lambda i: 30 - (i % 30))
df['T'] = df['DaysToExpiry'] / 365
df['T'] = df['T'].astype(float)

df['Delta'] = df.apply(lambda row: black_scholes_delta(
    S=float(row['Close']),
    K=float(row['Close']),         # strike price matches the close price, so it is at the money
    T=float(row['T']),
    r=0.01,
    sigma=0.2
), axis=1)

df['Price'] = df.apply(lambda row: black_scholes_price(
    S=float(row['Close']),
    K=float(row['Close']),         # strike price matches the close price, so it is at the money
    T=float(row['T']),
    r=0.01,
    sigma=0.2
), axis=1)

# reset index for precaution
df = df.reset_index(drop=True)

# generating the double axes plot
fig, ax1 = plt.subplots(figsize=(16, 8))

# plotting delta
ax1.set_xlabel('Date', fontsize=14)
ax1.set_ylabel('Delta', color='tab:blue', fontsize=14)
ax1.plot(df['Date'], df['Delta'], color='tab:blue', linewidth=2.0, label='Delta')
ax1.tick_params(axis='y', labelcolor='tab:blue', labelsize=12)
ax1.tick_params(axis='x', labelsize=12)
ax1.set_ylim(0.49, 0.55)

# adding vertical lines every 30 days (option "roll" markers)
for i in range(0, len(df), 30):
    ax1.axvline(x=df['Date'][i], color='gray', linestyle='--', linewidth=0.8, alpha=0.5)

# plotting price as the second axes
ax2 = ax1.twinx()
ax2.set_ylabel('Option Price ($)', color='tab:orange', fontsize=14)
ax2.plot(df['Date'], df['Price'], color='tab:orange', linewidth=2.0, label='Option Price')
ax2.tick_params(axis='y', labelcolor='tab:orange', labelsize=12)
ax2.set_ylim(0, df['Price'].max() * 1.1)

# annotating a price peak
peak_idx = df['Price'].idxmax()
peak_date = df['Date'][peak_idx]
peak_price = df['Price'][peak_idx]

ax2.plot(peak_date, peak_price, marker='o', color='red', markersize=9, label='Peak Option Price')

# creating a legend from both axes
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='best')

# title and final formatting
plt.title('SPY ETF 30-Day ATM Call Option: Delta and Price Over Last Decade (Black-Scholes)', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()




