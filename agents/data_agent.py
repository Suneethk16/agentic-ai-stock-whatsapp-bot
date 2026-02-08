import yfinance as yf
import pandas as pd
import os
import requests
from dotenv import load_dotenv
import feedparser
load_dotenv()

class DataAgent:
    def __init__(self):
        self.stock_symbol = os.getenv("STOCK_SYMBOL")


    def fetch_historical_data(self, period="3mo"):
        stock = yf.Ticker(self.stock_symbol)
        return stock.history(period=period)

    # PRIMARY news source
    def fetch_alpha_vantage_news(self):
        api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

        url = "https://www.alphavantage.co/query"
        params = {
            "function": "NEWS_SENTIMENT",
            "tickers": self.stock_symbol,
            "limit": 5,
            "apikey": api_key
        }

        response = requests.get(url, params=params)
        data = response.json()

        news_list = []

        for item in data.get("feed", []):
            news_list.append({
                "title": item.get("title"),
                "publisher": item.get("source"),
                "link": item.get("url"),
                "content": item.get("summary"),
                "sentiment": item.get("overall_sentiment_label")
            })

        return news_list


    def run(self):
        print(f"\n📊 Fetching data for {self.stock_symbol}...\n")

        # 1️⃣ Historical prices
        hist_data = self.fetch_historical_data()

        # 2️⃣ NEWS — THIS IS THE LINE YOU UPDATE 👇
        news_data = self.fetch_alpha_vantage_news()


        print("✅ Historical Data (last 5 rows):")
        print(hist_data.tail())

        print("\n📰 Latest News:")
        if not news_data:
            print("⚠️ No news found.")
        else:
            for i, news in enumerate(news_data, start=1):
                print(f"\n{i}. {news['title']}")
                print(f"   Source: {news['publisher']}")
                print(f"   Link: {news['link']}")

        return hist_data, news_data
