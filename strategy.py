from backtesting import Strategy
from black_scholes import black_scholes_delta

class DeltaStrategy(Strategy):
    def init(self):
        close = self.data.Close
        self.T = [ (30 - (i % 30)) / 365 for i in range(len(close)) ]  # Rolling expiry
        self.delta = [
            black_scholes_delta(S=close[i], K=close[i], T=self.T[i], r=0.01, sigma=0.2)
            for i in range(len(close))
        ]

    def next(self):
        if len(self.delta) < 2:
            return
        
        delta_prev = self.delta[-2]
        delta_curr = self.delta[-1]

        # Debug: Print deltas to confirm movement
        # print(f"delta_prev: {delta_prev:.4f}, delta_curr: {delta_curr:.4f}")

        if not self.position and delta_prev <= 0.515 and delta_curr > 0.515:
            self.buy()
        elif self.position and delta_prev >= 0.51 and delta_curr < 0.51:
            self.position.close()



