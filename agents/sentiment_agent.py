from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAgent:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_article(self, text):
        if not text:
            return {"compound": 0.0, "label": "Neutral"}

        score = self.analyzer.polarity_scores(text)
        compound = score["compound"]

        if compound >= 0.05:
            label = "Positive"
        elif compound <= -0.05:
            label = "Negative"
        else:
            label = "Neutral"

        return {
            "compound": compound,
            "label": label
        }

    def run(self, news_data):
        print("\n🧠 Performing sentiment analysis...\n")

        sentiment_results = []
        total_score = 0

        for news in news_data:
            content = news.get("content") or news.get("title")
            result = self.analyze_article(content)

            sentiment_results.append({
                "title": news["title"],
                "source": news["publisher"],
                "sentiment": result["label"],
                "score": result["compound"]
            })

            total_score += result["compound"]

        overall_score = (
            total_score / len(sentiment_results)
            if sentiment_results else 0
        )

        if overall_score >= 0.05:
            overall_sentiment = "Bullish 📈"
        elif overall_score <= -0.05:
            overall_sentiment = "Bearish 📉"
        else:
            overall_sentiment = "Neutral ⚖️"

        return sentiment_results, overall_sentiment
