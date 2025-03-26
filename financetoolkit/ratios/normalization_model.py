"""Normalization Module"""
__docformat__ = "google"

import pandas as pd

def get_zm_earnings_yield(
    earnings_per_share: pd.Series, market_price_per_share: pd.Series
) -> pd.Series:
    """
    Calculates the zero-max earnings yield ratio, which measures the earnings per share relative
    to the market price per share.

    Args:
        earnings_per_share (float or pd.Series): Earnings per share of the company.
        market_price_per_share (float or pd.Series): Market price per share of the company.

    Returns:
        float | pd.Series: The earnings yield ratio.
    """
    earnings_yield = earnings_per_share / market_price_per_share
    
    return earnings_yield.div(earnings_yield.max(axis=1), axis=0)


def get_zm_free_cash_flow_yield(
    free_cash_flow: float | pd.Series, market_capitalization: float | pd.Series
) -> pd.Series:
    """
    Calculates the zero-max free cash flow yield ratio, which measures the free cash flow
    relative to the market capitalization of the company.

    Args:
        free_cash_flow (float or pd.Series): Free cash flow of the company.
        market_capitalization (float or pd.Series): Market capitalization of the company.

    Returns:
        float | pd.Series: The free cash flow yield ratio.
    """
    free_cash_flow_yield = free_cash_flow / market_capitalization
    
    return free_cash_flow_yield.div(free_cash_flow_yield.max(axis=1), axis=0)


def get_zm_dividend_yield(
    dividends: pd.Series,
    stock_price: pd.Series,
) -> pd.Series:
    """
    Calculate the zero-max dividend yield ratio, a valuation ratio that measures the amount of
    dividends distributed per share of stock relative to the stock's price.

    Args:
        dividends (float or pd.Series): Dividend paid out by the company.
        stock_price (float or pd.Series): Stock price of the company.

    Returns:
        float | pd.Series: The dividend yield percentage value.
    """
    dividend_yield = dividends / stock_price
    
    return dividend_yield.div(dividend_yield.max(axis=1), axis=0)

def get_zm_shares_outstanding(
    shares_outstanding: pd.Series,
) -> pd.Series:
    """
    Calculate the zero-max ratio, a valuation ratio that measures the amount of
    shares are outstanding relative to the maximum shares outstanding within the
    period specified.

    Args:
        shares outstanding (float or pd.Series): Shares outstanding by the company.

    Returns:
        float | pd.Series: The zero-max shares outstanding value.
    """
    
    return shares_outstanding.div(shares_outstanding.max(axis=1), axis=0)
  
  
def get_zm_revenue(
    revenue: pd.Series,
) -> pd.Series:
    """
    Calculate the zero-max ratio, a valuation ratio that measures the amount of
    revenue relative to the maximum revenue within the
    period specified.

    Args:
        revenue (float or pd.Series): revenue earned by the company.

    Returns:
        float | pd.Series: The zero-max revenue value.
    """
    
    return revenue.div(revenue.max(axis=1), axis=0)