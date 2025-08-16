import pandas as pd

class Backtester:
    def __init__(self, strategy, initial_capital=10000):
        self.strategy = strategy
        self.initial_capital = initial_capital
        self.capital = initial_capital
        self.positions = pd.DataFrame(columns=['Date', 'Position', 'Price', 'Size'])
        self.trades = pd.DataFrame(columns=['Date', 'Trade', 'Price', 'Size', 'Capital'])

    def execute_trade(self, date, position, price, size):
        if position == 'buy':
            self.capital -= price * size
            self.positions = self.positions.append({'Date': date, 'Position': position, 'Price': price, 'Size': size}, ignore_index=True)
            self.trades = self.trades.append({'Date': date, 'Trade': 'buy', 'Price': price, 'Size': size, 'Capital': self.capital}, ignore_index=True)
        elif position == 'sell':
            self.capital += price * size
            self.positions = self.positions.append({'Date': date, 'Position': position, 'Price': price, 'Size': size}, ignore_index=True)
            self.trades = self.trades.append({'Date': date, 'Trade': 'sell', 'Price': price, 'Size': size, 'Capital': self.capital}, ignore_index=True)

    def run_backtest(self, historical_data):
        for index, row in historical_data.iterrows():
            date = row['Date']
            signal = self.strategy.generate_signal(row)  # Assuming strategy has a method to generate signals
            if signal == 'buy':
                self.execute_trade(date, 'buy', row['Close'], 1)  # Example size of 1
            elif signal == 'sell':
                self.execute_trade(date, 'sell', row['Close'], 1)  # Example size of 1

    def get_results(self):
        return {
            'Final Capital': self.capital,
            'Trades': self.trades,
            'Positions': self.positions
        }