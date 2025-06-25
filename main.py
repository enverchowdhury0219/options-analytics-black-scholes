from black_scholes import black_scholes_price, black_scholes_delta

S = 100
K = 100
T = 0.5
r = 0.01
sigma = 0.2

price = black_scholes_price(S, K, T, r, sigma, option_type='call')
delta = black_scholes_delta(S, K, T, r, sigma, option_type='call')

print(f"Call Option Price: ${price:.2f}")
print(f"Call Option Delta: {delta:.4f}")
