def calculate_accuracy(y_true, y_pred):
    """Calculate the accuracy of predictions."""
    return sum(y_true == y_pred) / len(y_true)

def calculate_precision(y_true, y_pred):
    """Calculate the precision of predictions."""
    true_positive = sum((y_true == 1) & (y_pred == 1))
    false_positive = sum((y_true == 0) & (y_pred == 1))
    return true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0

def calculate_recall(y_true, y_pred):
    """Calculate the recall of predictions."""
    true_positive = sum((y_true == 1) & (y_pred == 1))
    false_negative = sum((y_true == 1) & (y_pred == 0))
    return true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0

def calculate_f1_score(y_true, y_pred):
    """Calculate the F1 score of predictions."""
    precision = calculate_precision(y_true, y_pred)
    recall = calculate_recall(y_true, y_pred)
    return 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

def calculate_sharpe_ratio(returns, risk_free_rate=0):
    """Calculate the Sharpe Ratio."""
    excess_returns = returns - risk_free_rate
    return excess_returns.mean() / excess_returns.std() if excess_returns.std() > 0 else 0

def calculate_max_drawdown(returns):
    """Calculate the maximum drawdown."""
    cumulative_returns = (1 + returns).cumprod()
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    return drawdown.min() if not drawdown.empty else 0

def calculate_sortino_ratio(returns, risk_free_rate=0):
    """Calculate the Sortino Ratio."""
    excess_returns = returns - risk_free_rate
    downside_returns = excess_returns[excess_returns < 0]
    return excess_returns.mean() / downside_returns.std() if downside_returns.std() > 0 else 0
