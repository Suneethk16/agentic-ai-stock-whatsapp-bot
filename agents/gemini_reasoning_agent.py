import os
import google.generativeai as genai
from datetime import datetime


class GeminiReasoningAgent:
    def __init__(self):
        """
        Initialize Gemini model using API key from environment.
        """
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    # -----------------------------
    # Public entry point
    # -----------------------------
    def run(self, stock, sentiment, trends, news):
        """
        Generate a WhatsApp-ready market summary using Gemini.
        Falls back to deterministic logic if Gemini fails.
        """
        try:
            prompt = self.build_prompt(stock, sentiment, trends, news)
            response = self.model.generate_content(prompt)
            return response.text.strip()

        except Exception as e:
            print(f"⚠️ Gemini unavailable, using fallback reasoning: {e}")
            return self.fallback(stock, sentiment, trends, news)

    # -----------------------------
    # Prompt construction
    # -----------------------------
    def build_prompt(self, stock, sentiment, trends, news):
        """
        Build a clean, structured prompt for Gemini.
        """
        return f"""
You are a professional financial analysis assistant.

Generate a concise WhatsApp-ready daily stock summary.

Stock: {stock}
Date: {datetime.now().strftime('%d %b %Y')}

Overall Market Sentiment:
{sentiment}

Price Trends:
- 7 Days: {self.format_trend(trends.get('7_days'))}
- 30 Days: {self.format_trend(trends.get('30_days'))}
- 90 Days: {self.format_trend(trends.get('90_days'))}

Key News Headlines:
{self.format_news(news)}

Guidelines:
- Keep it under 12 lines
- Use emojis sparingly
- Be neutral and factual
- Include a short risk note
- Do NOT give financial advice
"""

    # -----------------------------
    # Helper: Trend formatting
    # -----------------------------
    def format_trend(self, trend):
        """
        Convert trend dictionary into human-readable string.
        """
        if not trend:
            return "Data not available"

        return (
            f"{trend['trend']} | "
            f"{trend['percent_change']}% "
            f"({trend['start_price']} → {trend['end_price']})"
        )

    # -----------------------------
    # Helper: News formatting
    # -----------------------------
    def format_news(self, news):
        """
        Format top news headlines for prompt or fallback.
        """
        if not news:
            return "- No significant news available"

        headlines = []
        for item in news[:3]:
            headlines.append(f"- {item['title']}")

        return "\n".join(headlines)

    # -----------------------------
    # Fallback reasoning (NO LLM)
    # -----------------------------
    def fallback(self, stock, sentiment, trends, news):
        """
        Deterministic fallback if Gemini API fails.
        Ensures system never crashes.
        """
        return f"""
📈 {stock} Stock Update – {datetime.now().strftime('%d %b %Y')}

Market Sentiment:
{sentiment}

7-Day Trend:
{self.format_trend(trends.get('7_days'))}

30-Day Trend:
{self.format_trend(trends.get('30_days'))}

Key News:
{self.format_news(news)}

⚠️ This is an automated market summary, not financial advice.
""".strip()
