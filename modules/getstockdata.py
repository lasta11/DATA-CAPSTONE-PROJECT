# -*- coding: utf-8 -*-
"""GetStockData.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1re-dh3zI9x5LOvF0fRjezKZMhOBSlVFf
"""

import yfinance as yf

def get_stock_data_with_news(comp_list, parsed_news, start_date='2020-01-01', end_date='2023-03-01'):
    """
    Returns stock data with sentiment scores for a given list of companies and parsed news data.

    Parameters:
    comp_list (list): A list of company tickers (strings).
    parsed_news (list): A list of news articles parsed from a website, each element is a list containing [ticker, date, headline, sentiment score].
    start_date (str): The start date in yyyy-mm-dd format for retrieving stock data. Default is '2020-01-01'.
    end_date (str): The end date in yyyy-mm-dd format for retrieving stock data. Default is '2023-03-01'.

    Returns:
    A pandas DataFrame with columns ['Date', 'Sentiment Score', 'Open', 'High', 'Low', 'Increase', 'Ticker'].
    """

    # Initialize an empty list to store the data
    dat = []

    # Set the ticker
    for comp in comp_list:
        # Get the stock data
        ticker = yf.Ticker(comp)
        data = ticker.history(start=start_date, end=end_date)
        data.reset_index(inplace=True)
        data = data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
        data['Increase'] = data['Close'].diff().apply(lambda x: 1 if x > 0 else 0)
        data.dropna(inplace=True)

        # Match the news articles to the corresponding dates in the stock data
        cr = [article for article in parsed_news if article[0] == comp]
        for article in cr:
            for ind, row in data.iterrows():
                if str(row['Date']).split()[0] == article[1]:
                    dat.append([str(row['Date']), article[-1], row['Open'], row['High'], row['Low'], row['Increase'], comp])
                    break

    # Convert the list to a pandas DataFrame and return it
    df = pd.DataFrame(dat, columns=['Date', 'Sentiment Score', 'Open', 'High', 'Low', 'Increase', 'Ticker'])
    return df