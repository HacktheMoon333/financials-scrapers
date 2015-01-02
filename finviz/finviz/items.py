# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Stock(scrapy.Item):
    n = scrapy.Field()
    ticker = scrapy.Field()
    company = scrapy.Field()
    sector = scrapy.Field()
    industry = scrapy.Field()
    country = scrapy.Field()
    market_cap = scrapy.Field()
    p_e = scrapy.Field()
    price = scrapy.Field()
    change = scrapy.Field()
    volume = scrapy.Field()

class Option(scrapy.Item):
    ticker = scrapy.Field()
    symbol = scrapy.Field()
    option = scrapy.Field()
    close = scrapy.Field()
    change = scrapy.Field()
    volume = scrapy.Field()
    volume_change = scrapy.Field()
    open_interest = scrapy.Field()
    open_interest_change = scrapy.Field()
    url = scrapy.Field()

class YahooSummary(scrapy.Item):
    ticker = scrapy.Field()
    prev_close = scrapy.Field()
    open = scrapy.Field()
    bid = scrapy.Field()
    ask = scrapy.Field()
    _1y_target_est = scrapy.Field()
    beta = scrapy.Field()
    next_earnings_date = scrapy.Field()
    day_s_range = scrapy.Field()
    _52wk_range = scrapy.Field()
    volume = scrapy.Field()
    avg_vol = scrapy.Field()
    market_cap = scrapy.Field()
    p_e = scrapy.Field()
    eps = scrapy.Field()
    div_yield = scrapy.Field()
    earnings_date = scrapy.Field()

class YahooKeyStats(scrapy.Item):
    ticker = scrapy.Field()
    market_cap = scrapy.Field()
    enterprise_value = scrapy.Field()
    trailing_p_e = scrapy.Field()
    forward_p_e = scrapy.Field()
    peg_ratio = scrapy.Field()
    price_sales = scrapy.Field()
    price_book = scrapy.Field()
    enterprise_value_revenue = scrapy.Field()
    enterprise_value_ebitda = scrapy.Field()
    fiscal_year_ends = scrapy.Field()
    most_recent_quarter = scrapy.Field()
    profit_margin = scrapy.Field()
    operating_margin = scrapy.Field()
    return_on_assets = scrapy.Field()
    return_on_equity = scrapy.Field()
    revenue = scrapy.Field()
    revenue_per_share = scrapy.Field()
    qtrly_revenue_growth = scrapy.Field()
    gross_profit = scrapy.Field()
    ebitda = scrapy.Field()
    net_income_avl_to_common = scrapy.Field()
    diluted_eps = scrapy.Field()
    qtrly_earnings_growth = scrapy.Field()
    total_cash = scrapy.Field()
    total_cash_per_share = scrapy.Field()
    total_debt = scrapy.Field()
    total_debt_equity = scrapy.Field()
    current_ratio = scrapy.Field()
    book_value_per_share = scrapy.Field()
    operating_cash_flow = scrapy.Field()
    levered_free_cash_flow = scrapy.Field()
    beta = scrapy.Field()
    _52_week_change_3 = scrapy.Field()
    s_p500_52_week_change_3 = scrapy.Field()
    _52_week_high = scrapy.Field()
    _52_week_low = scrapy.Field()
    _50_day_moving_average_3 = scrapy.Field()
    _200_day_moving_average_3 = scrapy.Field()
    avg_vol = scrapy.Field()
    avg_vol = scrapy.Field()
    shares_outstanding_5 = scrapy.Field()
    float = scrapy.Field()
    held_by_insiders_1 = scrapy.Field()
    held_by_institutions_1 = scrapy.Field()
    shares_short = scrapy.Field()
    short_ratio = scrapy.Field()
    short_of_float = scrapy.Field()
    shares_short = scrapy.Field()
    forward_annual_dividend_rate_4 = scrapy.Field()
    forward_annual_dividend_yield_4 = scrapy.Field()
    trailing_annual_dividend_yield_3 = scrapy.Field()
    trailing_annual_dividend_yield_3 = scrapy.Field()
    _5_year_average_dividend_yield_4 = scrapy.Field()
    payout_ratio_4 = scrapy.Field()
    dividend_date_3 = scrapy.Field()
    ex_dividend_date_4 = scrapy.Field()
    last_split_factor = scrapy.Field()
    last_split_date_3 = scrapy.Field()
