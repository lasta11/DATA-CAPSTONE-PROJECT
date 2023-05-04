# Web Scraping and Stock Price Prediction

This my repository for the work for my Senior year Capstone Project (Stock news collection using Web Scraping and Stock price prediction) using Machine Learning Models.

## Overview
The goal is to build a machine learning model which is capable to take historical stock news using API or web scraping, and perform sentiment analysis on the headline of the news to predict the future outcome of the news in the stock market. Also, see a relation of other assests affecting the stock market.

## Summary of Workdone

### Data

#### Web scraping to collect data:
For collecting the historical stock news I chose FinViz website. This website is a stock screener which has all stock information, market prices along with news related to each particular stock. Also it has updated information on the performance of each sector, industry and any major stock index. Below is a quick look how the stock news are arranged for each ticker, for example: 'AMZN'
   * ![pics](https://github.com/lasta11/DATA-CAPSTONE-PROJECT/blob/main/Example%20Images/Finviz%20News.png)

Using python to parse this website and get date, ticker, and the headline of the news over a period of time. I used libraries like BeautifulSoup, requests, json to parse the website, extract the news the HTML, which looks like this: 
  * ![pics](https://github.com/lasta11/DATA-CAPSTONE-PROJECT/blob/main/Example%20Images/HTML%20Scraping.png)
  
  As we can see that each news are stored into a table with id='news-table' bounded by <tr>tags for the time data and <a></a> tags for the news headline tags, also we can see use similar method to get the news URL if we want for further use.  

  
* Preprocessing/ Clean up:
  
  For the preprocessing part, I iterate through all tr tags from the previous step and get the text for date, time, ticker and headline. I further format it into a list of lists for each news headline in proper format of [['ticker1','YYYY-MM-DD', 'HH:MMPM', 'News Headline1'], ['ticker1','YYYY-MM-DD', 'HH:MMPM', 'News Headline2']]


### Problem Formulation:

* Sentiment Analysis
  
  First step, to the project after the stock news collection was to perform sentiment analysis on the news data collected and assign a compuund score -1 being the highest negative and 1 being the highest positive and 0 being neutral. For example for 'AMZN' the compound sentiment was:
  
  * ![pics](https://github.com/lasta11/DATA-CAPSTONE-PROJECT/blob/main/Example%20Images/CompoundStock%20Sentiment.png)
 
  I used Yahoo Finance to download the historical stock prices, which included date, open_stock, close_stock, high-stock, low_stock, volume_stock for that day. 
  
  * ![pics](https://github.com/lasta11/DATA-CAPSTONE-PROJECT/blob/main/Example%20Images/Sony-sentiment.png)
  
  Further, for relationship I tried to look for correlation between the stock prices and the sentiment score for the previous day. 
  
  * ![pics](https://github.com/lasta11/DATA-CAPSTONE-PROJECT/blob/main/Example%20Images/Sentiment%20Score.png)

 Further, plotting sentiment over date: 
  * ![pics](https://github.com/lasta11/DATA-CAPSTONE-PROJECT/blob/main/Example%20Images/Sony_sentiment-date.png)
  
 Further, plotting stock price over same time period: 
  * ![pics](https://github.com/lasta11/DATA-CAPSTONE-PROJECT/blob/main/Example%20Images/Stock%20price%20time.png)
  * ![pics](https://github.com/lasta11/DATA-CAPSTONE-PROJECT/blob/main/Example%20Images/Sony_sentiment_time.png)
  
* Prediction using Machine Learning

  After collection of sentiment score, historical price data, predicting the stock price in the future using machine learning models. I used ARIMA (Autoregressive Integrated Moving Average) model to make the predictions, giving input as both past values of the stock price and other features, semtimemt scores. 
  
### Training
Model 1: ARIMA Model Predictions: 
  
 * ![pics](https://github.com/lasta11/DATA-CAPSTONE-PROJECT/blob/main/Example%20Images/Predictions_SONY.png)
  
 * ![pics](https://github.com/lasta11/DATA-CAPSTONE-PROJECT/blob/main/Example%20Images/Pep_predictions.png)

Model 2: Neural Network Model with dropout regularization and train it using binary cross-entropy loss and Adam optimizer with a learning rate of 0.001 for 500 epochs.

The accuracy of the model was about 68% . 
 

### Challenges 
  
* The GPU of my computer was not the best one for web scraping, it would have been less time consuming with higher GPU.
  
  
### Future Work

  To train over more data, and other models like LSTM and compare the results with ARIMA model.
* WOrk with parameters to get more accurate predictions
* Incorporate the asset prices such as gold, silver, etc. to predict the prices along with the sentiment from their news and see if there is correlation between assets and stock news.

## How to reproduce results

### Overview of files in this repository:
  
  * modules



### Software Setup
* Packages used in notebook: numpy, pandas, matplotlib, tenserflow, sklearn, BeautifulSoup, requests, json, yfinance, seaborn, statsmodels.api
Tensorflow-metal PluggableDevice was installed to accelerate training with Metal on Mac GPUs using this link.


### References:
* https://www.kaggle.com/datasets/aaron7sun/stocknews
* https://github.com/kianso7414/News-Scraping/blob/main/scrape_final.ipynb
  


