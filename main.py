from black_scholes import black_scholes_delta, black_scholes_price
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

df['Price'] = df.apply(lambda row: black_scholes_price(
    S=float(row['Close']),
    K=float(row['Close']),         # ATM
    T=float(row['T']),
    r=0.01,
    sigma=0.2
), axis=1)

# Reset index just in case
df = df.reset_index(drop=True)

# Create plot
fig, ax1 = plt.subplots(figsize=(16, 8))

# Plot Delta
ax1.set_xlabel('Date', fontsize=14)
ax1.set_ylabel('Delta', color='tab:blue', fontsize=14)
ax1.plot(df['Date'], df['Delta'], color='tab:blue', linewidth=2.0, label='Delta')
ax1.tick_params(axis='y', labelcolor='tab:blue', labelsize=12)
ax1.tick_params(axis='x', labelsize=12)
ax1.set_ylim(0.49, 0.55)

# Add vertical lines every 30 days (option "roll" markers)
for i in range(0, len(df), 30):
    ax1.axvline(x=df['Date'][i], color='gray', linestyle='--', linewidth=0.8, alpha=0.5)

# Plot Option Price on second axis
ax2 = ax1.twinx()
ax2.set_ylabel('Option Price ($)', color='tab:red', fontsize=14)
ax2.plot(df['Date'], df['Price'], color='tab:red', linewidth=2.0, label='Option Price')
ax2.tick_params(axis='y', labelcolor='tab:red', labelsize=12)
ax2.set_ylim(0, df['Price'].max() * 1.1)

# Annotate a price peak
peak_idx = df['Price'].idxmax()
peak_date = df['Date'][peak_idx]
peak_price = df['Price'][peak_idx]

peak_delta_indx = df['Delta'].idxmax()
max_delta_date = df['Delta'][peak_delta_indx]
max_delta = df['Delta'][peak_delta_indx]

ax2.plot(peak_date, peak_price, marker='o', color='red', markersize=9, label='Peak Option Price')

# Combine legends from both axes
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='best')

# Title and layout
plt.title('SPY ETF 30-Day ATM Call Option: Delta and Price Over Last Decade (Black-Scholes)', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()




