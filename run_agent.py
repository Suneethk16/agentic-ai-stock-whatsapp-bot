from agents.data_agent import DataAgent
from agents.sentiment_agent import SentimentAgent
from agents.trend_agent import TrendAgent
from agents.reasoning_agent import ReasoningAgent
from agents.whatsapp_agent import WhatsAppAgent
from agents.gemini_reasoning_agent import GeminiReasoningAgent


import os

if __name__ == "__main__":
    data_agent = DataAgent()
    sentiment_agent = SentimentAgent()
    trend_agent = TrendAgent()
    gemini_agent = GeminiReasoningAgent()
    whatsapp_agent = WhatsAppAgent()

    # 1️⃣ Fetch data
    hist_data, news_data = data_agent.run()

    if not news_data:
        print("\n⚠️ No valid news found. WhatsApp message will NOT be sent.")
        exit(0)

    # 2️⃣ Analyze sentiment & trends
    sentiment_results, overall_sentiment = sentiment_agent.run(news_data)
    trend_results = trend_agent.run(hist_data)

    # 3️⃣ Reasoning
    final_message = gemini_agent.run(
        stock=os.getenv("STOCK_SYMBOL"),
        sentiment=overall_sentiment,
        trends=trend_results,
        news=news_data
    )

    print("\n📩 FINAL AGENT OUTPUT (WhatsApp-ready):\n")
    print(final_message)

    # 4️⃣ Send WhatsApp message
    sid = whatsapp_agent.send_message(final_message)

    print("\n📲 WhatsApp message sent successfully!")
    print(f"Message SID: {sid}")
