from datetime import datetime

class ReasoningAgent:
    def run(self, stock_symbol, sentiment_results, overall_sentiment, trend_results):
        print("\n🧠 Performing market reasoning...\n")

        short_term = trend_results.get("7_days")
        mid_term = trend_results.get("30_days")
        long_term = trend_results.get("90_days")

        confidence = "Medium"
        recommendation = "Hold"
        risk_note = ""

        # Core reasoning logic
        if "Bullish" in overall_sentiment and short_term and "Uptrend" in short_term["trend"]:
            recommendation = "Buy / Accumulate"
            confidence = "High"

        elif "Bearish" in overall_sentiment and short_term and "Downtrend" in short_term["trend"]:
            recommendation = "Sell / Avoid"
            confidence = "High"

        elif "Bullish" in overall_sentiment and short_term and "Downtrend" in short_term["trend"]:
            recommendation = "Wait for Confirmation"
            risk_note = "Positive news but short-term weakness detected."
            confidence = "Low"

        elif "Neutral" in overall_sentiment:
            recommendation = "Hold / Watch"
            confidence = "Medium"

        # Pick top 2 impactful news headlines
        top_news = sentiment_results[:2]

        summary = {
            "stock": stock_symbol,
            "date": datetime.now().strftime("%d %b %Y"),
            "overall_sentiment": overall_sentiment,
            "recommendation": recommendation,
            "confidence": confidence,
            "short_term_trend": short_term,
            "mid_term_trend": mid_term,
            "long_term_trend": long_term,
            "top_news": top_news,
            "risk_note": risk_note
        }

        return self.generate_message(summary)

    def generate_message(self, summary):
        message = (
            f"📈 Stock Insight: {summary['stock']}\n"
            f"🗓 Date: {summary['date']}\n\n"
            f"🔎 Market Sentiment: {summary['overall_sentiment']}\n"
        )

        if summary["short_term_trend"]:
            message += (
                f"📊 7-Day Trend: {summary['short_term_trend']['trend']} "
                f"({summary['short_term_trend']['percent_change']}%)\n"
            )

        if summary["mid_term_trend"]:
            message += (
                f"📊 30-Day Trend: {summary['mid_term_trend']['trend']} "
                f"({summary['mid_term_trend']['percent_change']}%)\n"
            )

        message += (
            f"\n💡 Recommendation: {summary['recommendation']}\n"
            f"🎯 Confidence: {summary['confidence']}\n\n"
            f"📰 Key News:\n"
        )

        for news in summary["top_news"]:
            message += f"- {news['title']} ({news['sentiment']})\n"

        if summary["risk_note"]:
            message += f"\n⚠️ Risk Note: {summary['risk_note']}\n"

        message += "\n⚠️ This is an AI-generated market insight, not financial advice."

        return message
